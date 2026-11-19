#!/usr/bin/env python3
"""Relier le contenu aux contrats gagnés : trois modèles d'attribution, en lecture seule.

Principe : on FIXE d'abord la question, la métrique, le modèle principal et la
fenêtre (commande `fixer`), puis seulement on produit le rapport. Le rapport
montre les trois modèles côte à côte et dit si le classement tient d'un modèle
à l'autre.

Modèles :
  premier-contact : tout le crédit au premier contenu vu avant la signature
  lineaire        : crédit égal à tous les contenus du parcours
  decroissance    : plus de crédit aux contenus proches de la signature
                    (demi-vie réglée dans le plan)

Entrées :
  --contrats fichier.json   liste de contrats :
        [{"montant": 12000, "date_signature": "2026-03-15",
          "parcours": [{"url": "/blog/exemple", "date": "2026-01-05"}, ...]}]
  --hubspot                 lit les affaires gagnées dans HubSpot (LECTURE SEULE,
                            jeton dans HUBSPOT_TOKEN). Parcours réduit à la première
                            et à la dernière page vue de chaque contact associé.
  --ga4-fichier f.json      visites par page : [{"page_path": "/blog/x", "sessions": 10,
                            "users": 8, "conversions": 1}]
  --ga4                     lit GA4 (LECTURE SEULE : GA4_PROPERTY_ID,
                            GA4_CREDENTIALS_JSON = fichier de compte de service)

Confidentialité : le rapport ne contient ni nom d'affaire, ni identifiant de
contrat ou de contact, ni adresse e-mail. Les adresses de page sont réduites à leur
chemin (sans paramètres) ; un segment contenant « @ » est masqué.

Aucune écriture dans HubSpot ni GA4. Aucune donnée d'exemple n'est jamais
substituée aux vraies données : une source illisible arrête le script.
"""
import argparse
import json
import math
import os
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

MODELES = ("premier-contact", "lineaire", "decroissance")
MIN_CONTRATS = 10          # en dessous, un classement est une anecdote
MAX_CONTRATS_LUS = 1000
BASE_HUBSPOT = "https://api.hubapi.com"

REGLES_DEFAUT = {
    "types": {
        "comparatif": ["/vs/", "/compar", "/alternative", "/versus"],
        "etude_de_cas": ["/case-stud", "/etude", "/cas-client", "/temoignage",
                         "/customer-stor", "/success-stor"],
        "webinaire": ["/webinar", "/webinaire", "/live/"],
        "podcast": ["/podcast/", "/episode"],
        "video": ["/video/", "/youtube/", "/watch/"],
        "outil": ["/outil", "/tool", "/calculat", "/grader", "/analyz"],
        "page_offre": ["/lp/", "/landing/", "/offre", "/telecharger", "/download/", "/audit"],
        "article": ["/blog/", "/articles/", "/article/", "/posts/", "/insights/"],
    },
    # ordre important : la première étape qui correspond l'emporte
    "etapes": {
        "decision": ["/pricing", "/tarif", "/demo", "/contact", "/essai", "/trial",
                     "/rendez-vous", "/devis", "/lp/", "/offre", "/audit"],
        "consideration": ["/case-stud", "/etude", "/cas-client", "/temoignage", "/webinar",
                          "/webinaire", "/guide", "/compar", "/vs/", "/alternative"],
        "decouverte": ["/blog", "/article", "/podcast", "/episode", "/video", "/insights"],
    },
}


class ErreurSource(Exception):
    pass


# ---------------------------------------------------------------------------
# Nettoyage
# ---------------------------------------------------------------------------

def normaliser_url(url):
    """Chemin seul, en minuscules, sans paramètres ; segments à « @ » masqués."""
    if not url:
        return ""
    u = str(url).strip()
    if "://" in u or u.startswith("//"):
        chemin = urlparse(u).path
    else:
        chemin = u.split("?")[0].split("#")[0]
    segments = [("[masque]" if "@" in s else s) for s in chemin.lower().split("/") if s]
    return "/" + "/".join(segments)


def lire_date(valeur):
    if not valeur:
        return None
    try:
        return date.fromisoformat(str(valeur)[:10])
    except ValueError:
        return None


def classer(url, regles, cle):
    for nom, motifs in regles[cle].items():
        if any(m in url for m in motifs):
            return nom
    return "autre" if cle == "types" else "inconnu"


# ---------------------------------------------------------------------------
# Préparation des contrats
# ---------------------------------------------------------------------------

def preparer_contrats(contrats, debut=None, fin=None):
    """Garde les contrats exploitables et compte ce qui est écarté."""
    qualite = {"recus": 0, "hors_fenetre": 0, "sans_montant": 0, "sans_date_signature": 0,
               "sans_parcours": 0, "touches_sans_date": 0, "touches_apres_signature": 0}
    prets = []
    for c in contrats:
        qualite["recus"] += 1
        signature = lire_date(c.get("date_signature"))
        try:
            montant = float(c.get("montant") or 0)
        except (TypeError, ValueError):
            montant = 0.0
        if signature is None:
            qualite["sans_date_signature"] += 1
            continue
        if (debut and signature < debut) or (fin and signature > fin):
            qualite["hors_fenetre"] += 1
            continue
        if montant <= 0:
            qualite["sans_montant"] += 1
            continue
        touches = []
        for t in c.get("parcours") or []:
            url = normaliser_url(t.get("url"))
            d = lire_date(t.get("date"))
            if not url:
                continue
            if d is None:
                qualite["touches_sans_date"] += 1
                continue
            if d > signature:     # un contenu vu après la signature n'a pas pu la causer
                qualite["touches_apres_signature"] += 1
                continue
            touches.append((d, url))
        if not touches:
            qualite["sans_parcours"] += 1
            continue
        touches.sort(key=lambda x: x[0])    # tri stable : l'ordre d'origine départage
        prets.append({"montant": montant, "signature": signature, "touches": touches})
    return prets, qualite


# ---------------------------------------------------------------------------
# Modèles d'attribution
# ---------------------------------------------------------------------------

def parts_du_contrat(contrat, modele, demi_vie):
    """Liste de (url, part) dont la somme vaut 1."""
    touches = contrat["touches"]
    if modele == "premier-contact":
        return [(touches[0][1], 1.0)]
    if modele == "lineaire":
        n = len(touches)
        return [(u, 1.0 / n) for _, u in touches]
    if modele == "decroissance":
        poids = [math.pow(0.5, (contrat["signature"] - d).days / demi_vie) for d, _ in touches]
        total = sum(poids)
        return [(u, p / total) for (_, u), p in zip(touches, poids)]
    raise ValueError(f"Modèle inconnu : {modele}")


def attribuer(contrats, modele, demi_vie):
    """url -> {"revenu": ..., "contrats_attribues": ...}"""
    res = defaultdict(lambda: {"revenu": 0.0, "contrats_attribues": 0.0})
    for c in contrats:
        for url, part in parts_du_contrat(c, modele, demi_vie):
            res[url]["revenu"] += c["montant"] * part
            res[url]["contrats_attribues"] += part
    return dict(res)


def classement(attrib, cle):
    return sorted(attrib, key=lambda u: (-attrib[u][cle], u))


# ---------------------------------------------------------------------------
# Rapport
# ---------------------------------------------------------------------------

def construire_rapport(contrats, plan, ga4=None, couts=None, regles=None):
    regles = regles or REGLES_DEFAUT
    debut, fin = lire_date(plan["debut"]), lire_date(plan["fin"])
    prets, qualite = preparer_contrats(contrats, debut, fin)
    n = len(prets)
    cle = "revenu" if plan["metrique"] == "revenu" else "contrats_attribues"
    demi_vie = plan["demi_vie_jours"]

    par_modele = {m: attribuer(prets, m, demi_vie) for m in MODELES}
    principal = par_modele[plan["modele_principal"]]
    ordre_principal = classement(principal, cle)
    rangs = {m: {u: i + 1 for i, u in enumerate(classement(par_modele[m], cle))} for m in MODELES}

    touches_par_url = defaultdict(set)
    for i, c in enumerate(prets):
        for _, u in c["touches"]:
            touches_par_url[u].add(i)

    visites = defaultdict(lambda: {"sessions": 0, "users": 0, "conversions": 0})
    for r in ga4 or []:
        v = visites[normaliser_url(r.get("page_path"))]
        for k in ("sessions", "users", "conversions"):
            v[k] += int(r.get(k) or 0)

    contenus = []
    for u in ordre_principal[:20]:
        v = visites.get(u, {"sessions": 0, "users": 0, "conversions": 0})
        contenus.append({
            "url": u, "type": classer(u, regles, "types"), "etape": classer(u, regles, "etapes"),
            "revenu": round(principal[u]["revenu"], 2),
            "contrats_attribues": round(principal[u]["contrats_attribues"], 2),
            "contrats_touches": len(touches_par_url[u]),
            "visites": v["sessions"], "conversions": v["conversions"],
            "revenu_par_visite": round(principal[u]["revenu"] / v["sessions"], 2) if v["sessions"] else None,
            "rang_par_modele": {m: rangs[m].get(u) for m in MODELES},
        })

    par_type = defaultdict(lambda: {"revenu": 0.0, "contrats_attribues": 0.0, "pages": 0, "visites": 0})
    for u, a in principal.items():
        t = par_type[classer(u, regles, "types")]
        t["revenu"] += a["revenu"]
        t["contrats_attribues"] += a["contrats_attribues"]
        t["pages"] += 1
        t["visites"] += visites.get(u, {}).get("sessions", 0)
    types = [{"type": k, "revenu": round(v["revenu"], 2),
              "contrats_attribues": round(v["contrats_attribues"], 2),
              "pages": v["pages"], "visites": v["visites"]}
             for k, v in sorted(par_type.items(), key=lambda kv: (-kv[1]["revenu"], kv[0]))]

    # stabilité du classement d'un modèle à l'autre
    tops = {m: set(classement(par_modele[m], cle)[:5]) for m in MODELES}
    taille = min((len(t) for t in tops.values()), default=0)
    commun = len(set.intersection(*tops.values())) if taille else 0
    stable = taille > 0 and commun >= math.ceil(taille * 0.6)

    # trous dans le parcours
    seuil = plan["seuil_trou_pct"]
    couverture = {e: 0 for e in regles["etapes"]}
    inconnues = 0
    total_touches = 0
    for c in prets:
        vues = set()
        for _, u in c["touches"]:
            e = classer(u, regles, "etapes")
            total_touches += 1
            if e == "inconnu":
                inconnues += 1
            else:
                vues.add(e)
        for e in vues:
            couverture[e] += 1
    trous = []
    for e, nb in couverture.items():
        pct = round(nb / n * 100, 1) if n else 0.0
        trous.append({"etape": e, "contrats_avec_cette_etape": nb, "couverture_pct": pct,
                      "sous_le_seuil": pct < seuil})

    couts_par_type = None
    if couts:
        couts_par_type = []
        for t in types:
            cout = float(couts.get(t["type"], 0) or 0)
            ca = t["contrats_attribues"]
            couts_par_type.append({
                "type": t["type"], "cout": cout, "revenu_attribue": t["revenu"],
                "contrats_attribues": ca,
                "cout_par_contrat_attribue": round(cout / ca, 2) if cout and ca else None,
                "revenu_par_unite_de_cout": round(t["revenu"] / cout, 2) if cout else None})

    moy_touches = round(sum(len(c["touches"]) for c in prets) / n, 1) if n else 0
    avertissements = []
    if n == 0:
        avertissements.append("Aucun contrat exploitable sur la fenêtre : rien à conclure.")
    elif n < MIN_CONTRATS:
        avertissements.append(
            f"Seulement {n} contrat(s) exploitable(s) : sous {MIN_CONTRATS}, chaque classement est une "
            "anecdote, pas une mesure. Lire les chiffres comme des exemples, pas comme des preuves.")
    ecartes_parcours = qualite["sans_parcours"]
    valides_avant_parcours = n + ecartes_parcours
    if valides_avant_parcours and ecartes_parcours / valides_avant_parcours > 0.5:
        avertissements.append(
            f"{ecartes_parcours} contrat(s) sur {valides_avant_parcours} n'ont aucun parcours exploitable : "
            "le suivi est trop incomplet pour attribuer sérieusement.")
    if n and moy_touches < 2.5:
        avertissements.append(
            f"Parcours très courts (moyenne {moy_touches} contenu(s) par contrat) : les modèles "
            "linéaire et décroissance se distinguent à peine du premier contact.")
    if n and not stable:
        avertissements.append(
            "Le haut du classement change selon le modèle : ne pas décider sur un seul modèle, "
            "et ne pas conclure sur ce rapport seul.")
    if total_touches and inconnues / total_touches > 0.4:
        avertissements.append(
            "Plus de 40 % des pages vues ne sont classées dans aucune étape : régler les règles "
            "d'adresses (--regles-url) avant de lire les trous.")
    if qualite["touches_apres_signature"]:
        avertissements.append(
            f"{qualite['touches_apres_signature']} page(s) vue(s) après la signature ont été ignorées.")

    return {
        "plan": plan,
        "genere_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "resume": {
            "contrats_exploitables": n,
            "montant_total": round(sum(c["montant"] for c in prets), 2),
            "montant_moyen": round(sum(c["montant"] for c in prets) / n, 2) if n else 0,
            "contenus_par_contrat_moyen": moy_touches,
            "devise": plan["devise"],
        },
        "qualite_des_donnees": qualite,
        "contenus_principaux": contenus,
        "par_type": types,
        "stabilite": {"top5_en_commun_entre_les_3_modeles": commun, "stable": stable},
        "trous_du_parcours": trous,
        "couts": couts_par_type,
        "avertissements": avertissements,
        "rappel": "Attribution n'est pas causalité : ce rapport classe des contenus vus avant une "
                  "signature, il ne prouve pas qu'ils l'ont provoquée.",
    }


def afficher_rapport(r):
    p, s = r["plan"], r["resume"]
    print("RELIER LE CONTENU AUX CONTRATS")
    print(f"Question : {p['question']}")
    print(f"Fixé le {p['fixe_le'][:10]} : métrique « {p['metrique']} », modèle principal "
          f"« {p['modele_principal']} », fenêtre du {p['debut']} au {p['fin']}")
    print(f"Contrats exploitables : {s['contrats_exploitables']} ; montant total {s['montant_total']:,.0f} "
          f"{s['devise']} ; {s['contenus_par_contrat_moyen']} contenu(s) par contrat en moyenne")
    q = r["qualite_des_donnees"]
    print(f"Qualité : {q['recus']} reçus, écartés : sans date de signature {q['sans_date_signature']}, "
          f"hors fenêtre {q['hors_fenetre']}, sans montant {q['sans_montant']}, sans parcours {q['sans_parcours']}")
    for a in r["avertissements"]:
        print(f"ATTENTION : {a}")
    print("\nContenus (modèle principal) :")
    for c in r["contenus_principaux"][:10]:
        rangs = "/".join(str(c["rang_par_modele"][m] or "-") for m in MODELES)
        print(f"  {c['url']} [{c['type']}, {c['etape']}] revenu {c['revenu']:,.0f} ; "
              f"{c['contrats_attribues']} contrat(s) ; rangs premier/linéaire/décroissance : {rangs}")
    print("\nPar type de contenu :")
    for t in r["par_type"]:
        print(f"  {t['type']} : revenu {t['revenu']:,.0f} ; {t['contrats_attribues']} contrat(s) ; "
              f"{t['pages']} page(s)")
    print("\nÉtapes du parcours présentes dans les contrats :")
    for t in r["trous_du_parcours"]:
        marque = " (sous le seuil)" if t["sous_le_seuil"] else ""
        print(f"  {t['etape']} : {t['couverture_pct']} %{marque}")
    if r["couts"]:
        print("\nCoûts :")
        for c in r["couts"]:
            print(f"  {c['type']} : coût {c['cout']:,.0f} ; par contrat attribué {c['cout_par_contrat_attribue']} ; "
                  f"revenu par unité de coût {c['revenu_par_unite_de_cout']}")
    print("\n" + r["rappel"])


# ---------------------------------------------------------------------------
# Sources en ligne (lecture seule)
# ---------------------------------------------------------------------------

def appel_http(methode, url, corps=None, entetes=None):
    data = json.dumps(corps).encode("utf-8") if corps is not None else None
    h = dict(entetes or {})
    if data is not None:
        h["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=methode, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        raise ErreurSource(f"HubSpot a répondu HTTP {e.code} (vérifier le jeton et ses droits de lecture).") from None
    except urllib.error.URLError as e:
        raise ErreurSource(f"HubSpot injoignable : {e.reason}") from None


def config_hubspot(env=None):
    env = os.environ if env is None else env
    return {
        "etape_gagnee": env.get("HUBSPOT_ETAPE_GAGNEE", "closedwon"),
        "p_url_debut": env.get("HUBSPOT_PROP_PREMIERE_URL", "hs_analytics_first_url"),
        "p_url_fin": env.get("HUBSPOT_PROP_DERNIERE_URL", "hs_analytics_last_url"),
        "p_date_debut": env.get("HUBSPOT_PROP_PREMIERE_DATE", "hs_analytics_first_visit_timestamp"),
        "p_date_fin": env.get("HUBSPOT_PROP_DERNIERE_DATE", "hs_analytics_last_visit_timestamp"),
    }


def charger_contrats_hubspot(http, debut, fin, jeton, config=None, pause=0.15):
    """Contrats gagnés avec un parcours à 2 points par contact (première et dernière page vue).

    Lecture seule : recherche d'affaires, associations, lecture de contacts.
    Rien de nominatif n'est gardé : ni nom d'affaire, ni identifiant, ni coordonnées.
    """
    cfg = config or config_hubspot()
    entetes = {"Authorization": f"Bearer {jeton}"}
    affaires, apres = [], None
    while True:
        corps = {"filterGroups": [{"filters": [
            {"propertyName": "dealstage", "operator": "EQ", "value": cfg["etape_gagnee"]},
            {"propertyName": "closedate", "operator": "GTE", "value": f"{debut}T00:00:00Z"},
            {"propertyName": "closedate", "operator": "LTE", "value": f"{fin}T23:59:59Z"}]}],
            "properties": ["amount", "closedate"], "limit": 100}
        if apres:
            corps["after"] = apres
        rep = http("POST", f"{BASE_HUBSPOT}/crm/v3/objects/deals/search", corps, entetes)
        affaires += rep.get("results", [])
        apres = rep.get("paging", {}).get("next", {}).get("after")
        time.sleep(pause)
        if not apres or len(affaires) >= MAX_CONTRATS_LUS:
            break
    props = [cfg["p_url_debut"], cfg["p_url_fin"], cfg["p_date_debut"], cfg["p_date_fin"]]
    contrats = []
    for a in affaires[:MAX_CONTRATS_LUS]:
        p = a.get("properties", {})
        assoc = http("GET", f"{BASE_HUBSPOT}/crm/v3/objects/deals/{a['id']}/associations/contacts",
                     None, entetes)
        ids = [r["id"] for r in assoc.get("results", [])][:5]
        parcours, vus = [], set()
        if ids:
            lus = http("POST", f"{BASE_HUBSPOT}/crm/v3/objects/contacts/batch/read",
                       {"properties": props, "inputs": [{"id": i} for i in ids]}, entetes)
            for ct in lus.get("results", []):
                cp = ct.get("properties", {})
                for k_url, k_date in ((cfg["p_url_debut"], cfg["p_date_debut"]),
                                      (cfg["p_url_fin"], cfg["p_date_fin"])):
                    if cp.get(k_url):
                        cle = (cp[k_url], str(cp.get(k_date) or "")[:10])
                        if cle not in vus:
                            vus.add(cle)
                            parcours.append({"url": cp[k_url], "date": cle[1]})
        time.sleep(pause)
        contrats.append({"montant": p.get("amount"), "date_signature": str(p.get("closedate") or "")[:10],
                         "parcours": parcours})
    return contrats


def charger_ga4(debut, fin, env=None):
    """Visites par page depuis GA4 (lecture seule). Non exécuté dans les tests."""
    env = os.environ if env is None else env
    prop, cred = env.get("GA4_PROPERTY_ID", ""), env.get("GA4_CREDENTIALS_JSON", "")
    if not prop or not cred:
        raise ErreurSource("GA4_PROPERTY_ID et GA4_CREDENTIALS_JSON sont requis pour --ga4.")
    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
    except ImportError:
        raise ErreurSource("Bibliothèque manquante : pip install google-analytics-data") from None
    metrique_conv = env.get("GA4_METRIQUE_CONVERSION", "keyEvents")
    try:
        client = BetaAnalyticsDataClient.from_service_account_json(cred)
        rep = client.run_report(RunReportRequest(
            property=f"properties/{prop}", dimensions=[Dimension(name="pagePath")],
            metrics=[Metric(name="sessions"), Metric(name="totalUsers"), Metric(name=metrique_conv)],
            date_ranges=[DateRange(start_date=debut, end_date=fin)], limit=10000))
    except Exception as e:  # message sans détail sensible
        raise ErreurSource(f"Lecture GA4 impossible ({type(e).__name__}). Vérifier la propriété, "
                           "le droit de lecture du compte de service et le nom de la métrique de conversion.") from None
    return [{"page_path": r.dimension_values[0].value, "sessions": int(r.metric_values[0].value),
             "users": int(r.metric_values[1].value), "conversions": int(float(r.metric_values[2].value))}
            for r in rep.rows]


# ---------------------------------------------------------------------------
# Commandes
# ---------------------------------------------------------------------------

def valider_plan(plan):
    d, f = lire_date(plan["debut"]), lire_date(plan["fin"])
    if not d or not f or d >= f:
        raise ValueError("Fenêtre invalide : --debut et --fin au format AAAA-MM-JJ, début avant fin.")
    if plan["modele_principal"] not in MODELES:
        raise ValueError(f"Modèle principal inconnu. Choix : {', '.join(MODELES)}")
    if plan["metrique"] not in ("revenu", "contrats"):
        raise ValueError("Métrique : revenu ou contrats.")
    if plan["demi_vie_jours"] <= 0:
        raise ValueError("La demi-vie doit être positive.")
    if not plan["question"].strip():
        raise ValueError("La question à laquelle ce rapport doit répondre est obligatoire.")


def cmd_fixer(args):
    plan = {"question": args.question, "metrique": args.metrique,
            "modele_principal": args.modele_principal, "debut": args.debut, "fin": args.fin,
            "demi_vie_jours": args.demi_vie, "devise": args.devise, "seuil_trou_pct": args.seuil_trou,
            "fixe_le": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    valider_plan(plan)
    Path(args.sortie).write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Plan de mesure fixé et enregistré : {args.sortie}")
    print("Il ne se modifie plus après avoir vu le résultat : un autre choix = un nouveau plan, daté.")


def lire_json(chemin, nom):
    try:
        return json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise ErreurSource(f"{nom} illisible ({chemin}) : {type(e).__name__}") from None


def cmd_rapport(args):
    plan = lire_json(args.plan, "Plan")
    valider_plan(plan)
    if bool(args.contrats) == bool(args.hubspot):
        raise ErreurSource("Choisir une source de contrats : --contrats fichier.json OU --hubspot.")
    if args.contrats:
        contrats = lire_json(args.contrats, "Fichier de contrats")
    else:
        jeton = os.environ.get("HUBSPOT_TOKEN") or os.environ.get("HUBSPOT_API_KEY", "")
        if not jeton:
            raise ErreurSource("Jeton HubSpot absent : définir HUBSPOT_TOKEN (droits de lecture des "
                               "affaires et des contacts uniquement).")
        contrats = charger_contrats_hubspot(appel_http, plan["debut"], plan["fin"], jeton)
    ga4 = None
    if args.ga4_fichier:
        ga4 = lire_json(args.ga4_fichier, "Fichier GA4")
    elif args.ga4:
        ga4 = charger_ga4(plan["debut"], plan["fin"])
    couts = lire_json(args.couts, "Fichier de coûts") if args.couts else None
    regles = lire_json(args.regles_url, "Règles d'adresses") if args.regles_url else None
    rapport = construire_rapport(contrats, plan, ga4, couts, regles)
    if args.sortie:
        Path(args.sortie).write_text(json.dumps(rapport, indent=2, ensure_ascii=False), encoding="utf-8")
    if args.json:
        print(json.dumps(rapport, indent=2, ensure_ascii=False))
    else:
        afficher_rapport(rapport)
        if args.sortie:
            print(f"\nRapport enregistré : {args.sortie}")


def construire_parseur():
    p = argparse.ArgumentParser(description="Relier le contenu aux contrats (lecture seule)")
    sub = p.add_subparsers(dest="commande", required=True)

    f = sub.add_parser("fixer", help="fixer la question, la métrique et le modèle AVANT de regarder")
    f.add_argument("--question", required=True)
    f.add_argument("--metrique", choices=["revenu", "contrats"], default="revenu")
    f.add_argument("--modele-principal", choices=MODELES, required=True)
    f.add_argument("--debut", required=True)
    f.add_argument("--fin", required=True)
    f.add_argument("--demi-vie", type=float, default=14.0,
                   help="jours, pour le modèle décroissance : à régler selon la durée du cycle de vente")
    f.add_argument("--devise", default="EUR")
    f.add_argument("--seuil-trou", type=float, default=30.0,
                   help="%% de contrats en dessous duquel une étape est signalée (repère arbitraire)")
    f.add_argument("--sortie", required=True)
    f.set_defaults(f=cmd_fixer)

    r = sub.add_parser("rapport", help="produire le rapport avec les trois modèles")
    r.add_argument("--plan", required=True)
    r.add_argument("--contrats")
    r.add_argument("--hubspot", action="store_true")
    r.add_argument("--ga4-fichier")
    r.add_argument("--ga4", action="store_true")
    r.add_argument("--couts", help='fichier JSON {"article": 1500, "video": 800}')
    r.add_argument("--regles-url", help="fichier JSON qui remplace les règles de classement des adresses")
    r.add_argument("--sortie")
    r.add_argument("--json", action="store_true")
    r.set_defaults(f=cmd_rapport)
    return p


def main(argv=None):
    for flux in (sys.stdout, sys.stderr):
        if hasattr(flux, "reconfigure"):
            flux.reconfigure(encoding="utf-8")
    args = construire_parseur().parse_args(argv)
    try:
        args.f(args)
    except (ErreurSource, ValueError) as e:
        print(f"Erreur : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
