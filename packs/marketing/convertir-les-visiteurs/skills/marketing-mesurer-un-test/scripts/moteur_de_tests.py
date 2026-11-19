#!/usr/bin/env python3
"""Moteur de tests marketing : créer, journaliser, scorer, suggérer.

Ce qu'il fait : tient un carnet local de tests (A/B ou jusqu'à 10 variantes),
calcule un verdict honnête et PROPOSE un gagnant. Il ne promeut rien tout seul :
adopter un gagnant est un geste humain (commande `valider`).

Règles de décision (fixées à la création, jamais retouchées après coup) :
  1. double seuil : écart significatif APRÈS correction des comparaisons
     multiples (Holm) ET écart utile (au moins `ecart_utile` %) ;
  2. aucun verdict avant le minimum d'échantillons par variante ;
  3. un résultat « sans différence » distingue « l'effet utile est écarté »
     de « le test n'a pas pu trancher ».

Deux types de mesure :
  - valeurs : une valeur par unité publiée (impressions d'un post, clics d'un
    envoi...). Test de Mann-Whitney + intervalle par rééchantillonnage.
  - taux    : des succès sur des essais (inscrits / visiteurs). Test exact de
    Fisher + intervalle par rééchantillonnage binomial.

Aucun appel réseau, aucune clé. Dépendances : numpy, scipy.
Les données restent dans un dossier local (option --dossier ou variable
MESURER_TESTS_DIR, sinon ./donnees-tests).
"""
import argparse
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy import stats

MAX_VARIANTES = 10
PLANCHER_VALEURS = 30      # unités minimales par variante (type valeurs)
PLANCHER_ESSAIS = 200      # essais minimaux par variante (type taux)
PLANCHER_SUCCES = 10       # succès minimaux par variante (type taux)
REPLICATS = 2000
GRAINE = 42

STATUTS_OUVERTS = ("en_cours", "non_concluant")

IDEES = {
    "page": ["titre_principal", "texte_du_bouton", "preuve_sociale", "longueur_du_formulaire",
             "image_principale", "ordre_des_sections"],
    "email": ["objet", "premiere_phrase", "longueur", "appel_a_l_action", "jour_et_heure_d_envoi",
              "delai_de_relance"],
    "linkedin": ["accroche", "format_du_post", "longueur", "appel_a_l_action", "heure_de_publication",
                 "visuel_ou_texte_seul"],
    "annonce": ["accroche", "visuel", "offre_mise_en_avant", "page_d_arrivee", "audience"],
    "seo": ["forme_du_titre", "description_de_page", "structure_des_intertitres",
            "maillage_interne", "longueur_du_contenu"],
}


# ---------------------------------------------------------------------------
# Fichiers
# ---------------------------------------------------------------------------

def maintenant():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def dossier_donnees(arg):
    d = Path(arg or os.environ.get("MESURER_TESTS_DIR") or "./donnees-tests")
    d.mkdir(parents=True, exist_ok=True)
    return d


def lire_json(chemin, defaut):
    if chemin.exists():
        return json.loads(chemin.read_text(encoding="utf-8"))
    return defaut


def ecrire_json(chemin, donnees):
    """Écriture atomique : fichier temporaire puis remplacement."""
    fd, tmp = tempfile.mkstemp(dir=str(chemin.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=2, ensure_ascii=False, default=str)
        os.replace(tmp, chemin)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


# ---------------------------------------------------------------------------
# Statistiques
# ---------------------------------------------------------------------------

def correction_holm(pvaleurs):
    """Holm-Bonferroni : p ajustées, dans l'ordre d'entrée."""
    m = len(pvaleurs)
    ordre = sorted(range(m), key=lambda i: pvaleurs[i])
    ajustees = [0.0] * m
    plus_haut = 0.0
    for rang, i in enumerate(ordre):
        val = min(1.0, (m - rang) * pvaleurs[i])
        plus_haut = max(plus_haut, val)
        ajustees[i] = plus_haut
    return ajustees


def _percentiles(ecarts, niveau):
    return (float(np.percentile(ecarts, niveau / 2 * 100)),
            float(np.percentile(ecarts, 100 - niveau / 2 * 100)))


def ic_ecart_valeurs(base, var, niveau, rng, replicats=REPLICATS):
    """Intervalle de l'écart relatif des moyennes (en %), par rééchantillonnage."""
    base = np.asarray(base, dtype=float)
    var = np.asarray(var, dtype=float)
    ecarts = []
    for _ in range(replicats):
        mb = rng.choice(base, size=len(base), replace=True).mean()
        if mb == 0:
            continue
        mv = rng.choice(var, size=len(var), replace=True).mean()
        ecarts.append((mv - mb) / mb * 100)
    if len(ecarts) < replicats // 2:
        return None, None
    return _percentiles(ecarts, niveau)


def ic_ecart_taux(s_base, n_base, s_var, n_var, niveau, rng, replicats=REPLICATS):
    """Intervalle de l'écart relatif des taux (en %), rééchantillonnage binomial."""
    pb, pv = s_base / n_base, s_var / n_var
    sb = rng.binomial(n_base, pb, size=replicats) / n_base
    sv = rng.binomial(n_var, pv, size=replicats) / n_var
    ok = sb > 0
    if ok.sum() < replicats // 2:
        return None, None
    ecarts = (sv[ok] - sb[ok]) / sb[ok] * 100
    return _percentiles(ecarts, niveau)


def p_mann_whitney(base, var):
    try:
        return float(stats.mannwhitneyu(base, var, alternative="two-sided")[1])
    except ValueError:  # toutes les valeurs identiques
        return 1.0


def p_fisher(s_base, n_base, s_var, n_var):
    table = [[s_base, n_base - s_base], [s_var, n_var - s_var]]
    return float(stats.fisher_exact(table, alternative="two-sided")[1])


# ---------------------------------------------------------------------------
# Évaluation d'un test (fonction pure : testable sans fichier)
# ---------------------------------------------------------------------------

def plancher(type_mesure):
    return PLANCHER_VALEURS if type_mesure == "valeurs" else PLANCHER_ESSAIS


def regrouper(test):
    """Retourne {variante: {"valeurs": [...]} ou {"succes": S, "essais": N}}."""
    if test["type"] == "valeurs":
        g = {v: {"valeurs": []} for v in test["variantes"]}
        for p in test["points"]:
            g[p["variante"]]["valeurs"].append(float(p["valeur"]))
    else:
        g = {v: {"succes": 0, "essais": 0, "points": 0} for v in test["variantes"]}
        for p in test["points"]:
            g[p["variante"]]["succes"] += int(p["succes"])
            g[p["variante"]]["essais"] += int(p["essais"])
            g[p["variante"]]["points"] += 1
    return g


def avancement(test, groupes):
    """Pour chaque variante : (acquis, requis, ok, libelle)."""
    requis = test["min_echantillons"]
    out = {}
    for v, g in groupes.items():
        if test["type"] == "valeurs":
            n = len(g["valeurs"])
            out[v] = {"acquis": n, "requis": requis, "ok": n >= requis, "unite": "valeurs"}
        else:
            ok = g["essais"] >= requis and g["succes"] >= PLANCHER_SUCCES
            out[v] = {"acquis": g["essais"], "requis": requis, "ok": ok, "unite": "essais",
                      "succes": g["succes"], "succes_requis": PLANCHER_SUCCES}
    return out


def evaluer(test, graine=GRAINE):
    """Calcule le verdict d'un test. Ne modifie pas `test`."""
    groupes = regrouper(test)
    avanc = avancement(test, groupes)
    if not all(a["ok"] for a in avanc.values()):
        return {"statut": "en_cours", "raison": "pas assez de données pour conclure",
                "avancement": avanc,
                "message": "Aucun verdict avant le minimum prévu par variante : regarder les "
                           "résultats avant ce seuil fausse la décision."}

    base_nom = test["variantes"][0]
    autres = test["variantes"][1:]
    alpha = test["alpha"]
    ecart_utile = test["ecart_utile"]
    signe = 1.0 if test["sens"] == "hausse" else -1.0
    niveau_ic = alpha / len(autres)   # intervalle ajusté au nombre de comparaisons
    rng = np.random.default_rng(graine)

    brutes = []
    details = []
    for v in autres:
        if test["type"] == "valeurs":
            b, x = groupes[base_nom]["valeurs"], groupes[v]["valeurs"]
            mb, mx = float(np.mean(b)), float(np.mean(x))
            ecart = (mx - mb) / mb * 100 if mb != 0 else None
            p = p_mann_whitney(b, x)
            lo, hi = ic_ecart_valeurs(b, x, niveau_ic, rng) if mb != 0 else (None, None)
            med_b, med_x = float(np.median(b)), float(np.median(x))
            alerte = None
            if ecart is not None and med_b != 0:
                ecart_med = (med_x - med_b) / med_b * 100
                if ecart * ecart_med < 0:
                    alerte = ("la moyenne et la médiane vont dans des sens opposés : le résultat "
                              "dépend de quelques valeurs extrêmes")
            d = {"variante": v, "n": len(x), "moyenne": round(mx, 3), "moyenne_base": round(mb, 3)}
        else:
            gb, gx = groupes[base_nom], groupes[v]
            tb, tx = gb["succes"] / gb["essais"], gx["succes"] / gx["essais"]
            ecart = (tx - tb) / tb * 100
            p = p_fisher(gb["succes"], gb["essais"], gx["succes"], gx["essais"])
            lo, hi = ic_ecart_taux(gb["succes"], gb["essais"], gx["succes"], gx["essais"],
                                   niveau_ic, rng)
            alerte = None
            d = {"variante": v, "n": gx["essais"], "taux": round(tx, 5), "taux_base": round(tb, 5)}
        amelioration = None if ecart is None else signe * ecart
        if lo is None:
            ic = None
        else:
            a, b_ = signe * lo, signe * hi
            ic = [round(min(a, b_), 1), round(max(a, b_), 1)]
        d.update({"ecart_pct": None if ecart is None else round(ecart, 1),
                  "amelioration_pct": None if amelioration is None else round(amelioration, 1),
                  "ic": ic, "p_brute": p, "alerte": alerte})
        brutes.append(p)
        details.append(d)

    ajustees = correction_holm(brutes)
    for d, pa in zip(details, ajustees):
        d["p_ajustee"] = round(pa, 4)
        d["p_brute"] = round(d["p_brute"], 4)
        am = d["amelioration_pct"]
        significatif = pa < alpha
        if am is None:
            d["verdict"] = "reference_a_zero"
        elif significatif and am >= ecart_utile:
            d["verdict"] = "gagnante"
        elif significatif and am > 0:
            d["verdict"] = "meilleure_ecart_faible"
        elif significatif and am < 0:
            d["verdict"] = "moins_bonne"
        else:
            d["verdict"] = "pas_de_difference_nette"

    verdicts = [d["verdict"] for d in details]
    if "gagnante" in verdicts:
        meilleure = max((d for d in details if d["verdict"] == "gagnante"),
                        key=lambda d: d["amelioration_pct"])
        statut = "gagnant_propose"
        message = (f"Proposition à valider par une personne : « {meilleure['variante']} » "
                   f"({meilleure['amelioration_pct']:+.1f} % sur la référence, p ajustée "
                   f"{meilleure['p_ajustee']}). Rien n'est appliqué tant que `valider` n'est pas lancé.")
        gagnant = meilleure["variante"]
    else:
        gagnant = None
        if all(v == "moins_bonne" for v in verdicts):
            statut = "base_conservee"
            message = "Toutes les variantes sont nettement moins bonnes : garder la référence."
        elif "meilleure_ecart_faible" in verdicts and "reference_a_zero" not in verdicts:
            statut = "ecart_trop_faible"
            message = ("Une variante est meilleure de façon significative, mais l'écart reste sous "
                       f"l'écart utile de {ecart_utile} % : ne justifie pas à lui seul de changer.")
        elif any(d["verdict"] == "reference_a_zero" for d in details):
            statut = "non_concluant"
            message = "La référence vaut zéro : l'écart relatif n'est pas défini, mesurer autrement."
        else:
            peut_cacher = any(
                d["ic"] is None or d["ic"][1] >= ecart_utile
                for d in details if d["verdict"] == "pas_de_difference_nette")
            if peut_cacher:
                statut = "non_concluant"
                message = ("Aucune différence nette, mais l'intervalle laisse la place à un écart "
                           "utile : le test n'a pas pu trancher. Ce n'est pas la preuve que les "
                           "variantes se valent. Prolonger (commande `etendre`) ou arrêter.")
            else:
                statut = "sans_difference"
                message = ("Aucune différence nette, et l'intervalle écarte un gain utile : "
                           "garder la variante la plus simple ou la moins chère.")

    return {"statut": statut, "gagnant": gagnant, "message": message, "variantes": details,
            "reference": base_nom, "alpha": alpha, "ecart_utile": ecart_utile,
            "comparaisons": len(autres), "correction": "Holm",
            "evalue_le": maintenant()}


# ---------------------------------------------------------------------------
# Commandes
# ---------------------------------------------------------------------------

def prochain_id(tests):
    nums = [int(t["id"].split("-")[1]) for t in tests if t["id"].startswith("TEST-")]
    return f"TEST-{(max(nums) if nums else 0) + 1:03d}"


def trouver(tests, ident):
    for t in tests:
        if t["id"] == ident:
            return t
    sys.exit(f"Test introuvable : {ident}")


def cmd_creer(args):
    d = dossier_donnees(args.dossier)
    tests = lire_json(d / "tests.json", [])
    try:
        variantes = json.loads(args.variantes)
    except json.JSONDecodeError:
        sys.exit('--variantes doit être une liste JSON, par exemple \'["actuelle","nouvelle"]\'')
    if (not isinstance(variantes, list) or not all(isinstance(v, str) and v for v in variantes)
            or len(set(variantes)) != len(variantes)):
        sys.exit("--variantes : liste de noms texte, tous différents")
    if not 2 <= len(variantes) <= MAX_VARIANTES:
        sys.exit(f"Il faut entre 2 et {MAX_VARIANTES} variantes (la première est la référence).")
    min_ech = args.min_echantillons or plancher(args.type)
    if min_ech < plancher(args.type):
        sys.exit(f"Minimum trop bas : {plancher(args.type)} au moins par variante pour le type "
                 f"« {args.type} ». En dessous, le test crie « gagnant » sur du bruit.")
    if not 0 < args.alpha < 0.2:
        sys.exit("--alpha doit être entre 0 et 0,2 (0,05 par défaut)")
    if args.ecart_utile <= 0:
        sys.exit("--ecart-utile doit être positif (en %)")
    test = {
        "id": prochain_id(tests), "canal": args.canal, "hypothese": args.hypothese,
        "variable": args.variable, "variantes": variantes, "metrique": args.metrique,
        "type": args.type, "sens": args.sens, "alpha": args.alpha,
        "ecart_utile": args.ecart_utile, "min_echantillons": min_ech,
        "statut": "en_cours", "cree_le": maintenant(), "points": [], "resultat": None,
        "gagnant": None, "historique": [],
    }
    tests.append(test)
    ecrire_json(d / "tests.json", tests)
    print(f"Test créé : {test['id']} : {args.hypothese}")
    print(f"  Variable : {args.variable} | canal : {args.canal} | mesure : {args.metrique} "
          f"({args.type}, {args.sens} = mieux)")
    print(f"  Variantes : {variantes} (référence : {variantes[0]})")
    print(f"  Règle fixée : p ajustée < {args.alpha} ET écart utile >= {args.ecart_utile} %, "
          f"minimum {min_ech} {'valeurs' if args.type == 'valeurs' else 'essais'} par variante")
    if len(variantes) > 4:
        print("  Attention : plus de 4 variantes durcit la correction et demande beaucoup plus de "
              "données ; réduire si le volume est faible.")


def cmd_journaliser(args):
    d = dossier_donnees(args.dossier)
    tests = lire_json(d / "tests.json", [])
    t = trouver(tests, args.id)
    if t["statut"] not in STATUTS_OUVERTS:
        sys.exit(f"{t['id']} est clos ({t['statut']}) : on n'y ajoute plus de données.")
    if args.variante not in t["variantes"]:
        sys.exit(f"Variante inconnue : {args.variante}. Variantes : {t['variantes']}")
    if t["type"] == "valeurs":
        if args.valeurs is not None:
            try:
                lot = [float(x) for x in json.loads(args.valeurs)]
            except (json.JSONDecodeError, TypeError, ValueError):
                sys.exit("--valeurs doit être une liste JSON de nombres")
        elif args.valeur is not None:
            lot = [args.valeur]
        else:
            sys.exit("Ce test mesure des valeurs : donner --valeur ou --valeurs")
        for x in lot:
            t["points"].append({"variante": args.variante, "valeur": x,
                                "note": args.note or "", "date": maintenant()})
        ecrire_json(d / "tests.json", tests)
        print(f"{len(lot)} mesure(s) ajoutée(s) à {t['id']} (variante « {args.variante} »).")
        return
    else:
        if args.succes is None or args.essais is None:
            sys.exit("Ce test mesure un taux : donner --succes et --essais")
        if args.essais <= 0 or not 0 <= args.succes <= args.essais:
            sys.exit("--essais doit être positif et --succes compris entre 0 et --essais")
        point = {"variante": args.variante, "succes": args.succes, "essais": args.essais}
    point["note"] = args.note or ""
    point["date"] = maintenant()
    t["points"].append(point)
    ecrire_json(d / "tests.json", tests)
    print(f"Mesure ajoutée à {t['id']} (variante « {args.variante} »).")


def afficher_evaluation(t, res, en_json=False):
    if en_json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return
    print(f"{t['id']} : {t['hypothese']}")
    if res["statut"] == "en_cours":
        print("  Pas encore de verdict : " + res["raison"])
        for v, a in res["avancement"].items():
            extra = ""
            if a["unite"] == "essais":
                extra = f", succès {a['succes']}/{a['succes_requis']}"
            print(f"   - {v} : {a['acquis']}/{a['requis']} {a['unite']}{extra}")
        print("  " + res["message"])
        return
    print(f"  Référence : {res['reference']} | correction : {res['correction']} sur "
          f"{res['comparaisons']} comparaison(s)")
    for d in res["variantes"]:
        ic = "n/a" if d["ic"] is None else f"[{d['ic'][0]}, {d['ic'][1]}] %"
        am = "n/a" if d["amelioration_pct"] is None else f"{d['amelioration_pct']:+.1f} %"
        print(f"   - {d['variante']} : amélioration {am}, intervalle {ic}, "
              f"p ajustée {d['p_ajustee']} : {d['verdict']}")
        if d["alerte"]:
            print(f"     Alerte : {d['alerte']}")
    print(f"  Statut : {res['statut']}")
    print("  " + res["message"])


def cmd_scorer(args):
    d = dossier_donnees(args.dossier)
    tests = lire_json(d / "tests.json", [])
    t = trouver(tests, args.id)
    if t["statut"] not in STATUTS_OUVERTS:
        print(f"{t['id']} est déjà clos ({t['statut']}). Verdict enregistré :")
        if t["resultat"]:
            afficher_evaluation(t, t["resultat"], args.json)
        return
    res = evaluer(t)
    afficher_evaluation(t, res, args.json)
    if res["statut"] == "en_cours":
        return
    t["resultat"] = res
    t["statut"] = res["statut"]
    t["gagnant"] = res.get("gagnant")
    ecrire_json(d / "tests.json", tests)


def cmd_etendre(args):
    d = dossier_donnees(args.dossier)
    tests = lire_json(d / "tests.json", [])
    t = trouver(tests, args.id)
    if t["statut"] != "non_concluant":
        sys.exit("On ne prolonge qu'un test non concluant.")
    if args.min_echantillons <= t["min_echantillons"]:
        sys.exit("Le nouveau minimum doit dépasser l'ancien.")
    t["historique"].append({"le": maintenant(), "action": "prolongation",
                            "ancien_minimum": t["min_echantillons"],
                            "nouveau_minimum": args.min_echantillons})
    t["min_echantillons"] = args.min_echantillons
    t["statut"] = "en_cours"
    ecrire_json(d / "tests.json", tests)
    print(f"{t['id']} prolongé jusqu'à {args.min_echantillons} par variante. Décision tracée : "
          "ne scorer qu'une fois ce nouveau minimum atteint.")


def cmd_lister(args):
    d = dossier_donnees(args.dossier)
    tests = lire_json(d / "tests.json", [])
    if not tests:
        print("Aucun test pour l'instant.")
        return
    comptes = {}
    for t in tests:
        comptes[t["statut"]] = comptes.get(t["statut"], 0) + 1
    print("Résumé : " + ", ".join(f"{k} {v}" for k, v in sorted(comptes.items())))
    attente = [t["id"] for t in tests if t["statut"] == "gagnant_propose"]
    if attente:
        print("À valider par une personne : " + ", ".join(attente))
    for t in tests:
        if args.statut != "tous" and t["statut"] != args.statut:
            continue
        print(f"- {t['id']} [{t['statut']}] {t['hypothese']} "
              f"(variable : {t['variable']}, {len(t['points'])} mesure(s))")


def cmd_valider(args):
    d = dossier_donnees(args.dossier)
    tests = lire_json(d / "tests.json", [])
    t = trouver(tests, args.id)
    if t["statut"] != "gagnant_propose":
        sys.exit("Seul un test au statut « gagnant_propose » peut être validé ou refusé.")
    carnet = lire_json(d / "carnet.json", {})
    if args.decision == "oui":
        r = next(v for v in t["resultat"]["variantes"] if v["variante"] == t["gagnant"])
        carnet[t["variable"]] = {
            "retenu": t["gagnant"], "reference": t["variantes"][0], "metrique": t["metrique"],
            "amelioration_pct": r["amelioration_pct"], "ic": r["ic"], "p_ajustee": r["p_ajustee"],
            "test": t["id"], "valide_le": maintenant(), "note": args.note or "",
        }
        ecrire_json(d / "carnet.json", carnet)
        t["statut"] = "gagnant_valide"
        print(f"Validé : « {t['gagnant']} » entre au carnet pour « {t['variable']} ». "
              "Le changement réel dans l'outil reste à faire par une personne.")
    else:
        t["statut"] = "gagnant_refuse"
        print(f"Refusé : {t['id']} reste dans l'historique, le carnet n'est pas modifié.")
    t["historique"].append({"le": maintenant(), "action": f"validation_{args.decision}",
                            "note": args.note or ""})
    ecrire_json(d / "tests.json", tests)


def cmd_carnet(args):
    d = dossier_donnees(args.dossier)
    carnet = lire_json(d / "carnet.json", {})
    if not carnet:
        print("Carnet vide : aucun gagnant validé.")
        return
    for variable, e in carnet.items():
        ic = "n/a" if not e["ic"] else f"[{e['ic'][0]}, {e['ic'][1]}] %"
        print(f"- {variable} : « {e['retenu']} » contre « {e['reference']} » sur {e['metrique']} "
              f"({e['amelioration_pct']:+.1f} %, intervalle {ic}, test {e['test']}, "
              f"validé le {e['valide_le'][:10]})")


def cmd_suggerer(args):
    d = dossier_donnees(args.dossier)
    tests = lire_json(d / "tests.json", [])
    if args.canal not in IDEES:
        sys.exit("Canal inconnu. Canaux connus : " + ", ".join(sorted(IDEES)))
    carnet = lire_json(d / "carnet.json", {})
    pris = set(carnet)
    pris.update(t["variable"] for t in tests
                if t["canal"] == args.canal and t["statut"] in STATUTS_OUVERTS + ("gagnant_propose",))
    inedits = [v for v in IDEES[args.canal] if v not in pris]
    vus = [t["variable"] for t in tests
           if t["canal"] == args.canal and t["statut"] in ("sans_difference", "ecart_trop_faible")]
    if inedits:
        print(f"Variables pas encore testées sur « {args.canal} » (3 premières) :")
        for v in inedits[:3]:
            print(f"  - {v}")
        print("Choisir celle qui touche le plus de monde et se change le plus facilement.")
    else:
        print("Toutes les variables courantes de ce canal sont testées ou en cours.")
    if vus:
        print("Déjà testées sans effet utile (à ne rejouer que si le contexte a changé) : "
              + ", ".join(sorted(set(vus))))


def construire_parseur():
    p = argparse.ArgumentParser(description="Moteur de tests marketing (local, sans réseau)")
    p.add_argument("--dossier", help="dossier des données (défaut : MESURER_TESTS_DIR ou ./donnees-tests)")
    sub = p.add_subparsers(dest="commande", required=True)

    c = sub.add_parser("creer", help="créer un test et fixer sa règle de décision")
    c.add_argument("--canal", required=True)
    c.add_argument("--hypothese", required=True)
    c.add_argument("--variable", required=True)
    c.add_argument("--variantes", required=True, help='liste JSON ; la première est la référence')
    c.add_argument("--metrique", required=True)
    c.add_argument("--type", choices=["valeurs", "taux"], default="valeurs")
    c.add_argument("--sens", choices=["hausse", "baisse"], default="hausse",
                   help="hausse : plus haut est mieux ; baisse : plus bas est mieux")
    c.add_argument("--alpha", type=float, default=0.05)
    c.add_argument("--ecart-utile", type=float, default=15.0,
                   help="écart relatif minimal (en %%) qui justifie de changer")
    c.add_argument("--min-echantillons", type=int, default=None)
    c.set_defaults(f=cmd_creer)

    j = sub.add_parser("journaliser", help="ajouter une mesure")
    j.add_argument("--id", required=True)
    j.add_argument("--variante", required=True)
    j.add_argument("--valeur", type=float)
    j.add_argument("--valeurs", help="plusieurs valeurs d'un coup : liste JSON, par exemple [12, 15, 9]")
    j.add_argument("--succes", type=int)
    j.add_argument("--essais", type=int)
    j.add_argument("--note", default="")
    j.set_defaults(f=cmd_journaliser)

    s = sub.add_parser("scorer", help="calculer le verdict (aucun avant le minimum)")
    s.add_argument("--id", required=True)
    s.add_argument("--json", action="store_true")
    s.set_defaults(f=cmd_scorer)

    e = sub.add_parser("etendre", help="prolonger un test non concluant (décision tracée)")
    e.add_argument("--id", required=True)
    e.add_argument("--min-echantillons", type=int, required=True)
    e.set_defaults(f=cmd_etendre)

    li = sub.add_parser("lister", help="état des tests")
    li.add_argument("--statut", default="tous")
    li.set_defaults(f=cmd_lister)

    v = sub.add_parser("valider", help="geste humain : adopter ou refuser un gagnant proposé")
    v.add_argument("--id", required=True)
    v.add_argument("--decision", choices=["oui", "non"], required=True)
    v.add_argument("--note", default="")
    v.set_defaults(f=cmd_valider)

    ca = sub.add_parser("carnet", help="gagnants validés par une personne")
    ca.set_defaults(f=cmd_carnet)

    su = sub.add_parser("suggerer", help="proposer la prochaine variable à tester")
    su.add_argument("--canal", required=True)
    su.set_defaults(f=cmd_suggerer)
    return p


def main(argv=None):
    for flux in (sys.stdout, sys.stderr):
        if hasattr(flux, "reconfigure"):
            flux.reconfigure(encoding="utf-8")
    args = construire_parseur().parse_args(argv)
    args.f(args)


if __name__ == "__main__":
    main()
