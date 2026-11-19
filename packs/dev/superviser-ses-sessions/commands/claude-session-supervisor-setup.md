---
description: Vérifie que le superviseur peut réellement lire tes transcripts et relancer tes sessions, et explique ce qu'il fait — ou ne fait que la moitié — selon ce qui est disponible ici.
argument-hint: "[--uninstall]"
---

# Setup — claude-session-supervisor

Tu exécutes le setup de ce pack. Trois fonctions, **dans cet ordre** : VÉRIFIER, INSTALLER, EXPLIQUER.

> ⚠️ **Le verdict se CALCULE**, chaque ligne vient d'une sonde. **« Non vérifiable » est une réponse
> autorisée** ; une case cochée sans mesure est pire qu'une case absente.
>
> 🪞 **Et attention au piège que ce pack enseigne lui-même** : une mesure par mot-clé **se trouve
> elle-même**. Si tu comptes les sessions depuis cette session, **exclus-toi** du compte — sinon
> l'instrument fabrique le signal qu'il cherche, et toujours dans le sens rassurant.

## Si l'argument est `--uninstall`

Ce pack **n'écrit rien** : ni fichier, ni configuration, ni dossier. Il lit des transcripts et envoie
des messages. **Rien à retirer** — désinstaller le plugin suffit.

Ne cherche aucun fichier à nettoyer : en inventer laisserait croire que le pack en avait posé.

## 1 — VÉRIFIER

Ce pack a **deux** capacités, et elles se dégradent **séparément**. C'est le cœur du diagnostic :
avec la première seule, il reste utile ; sans elle, il ne sert à rien.

**a) Lire les transcripts** — la capacité **vitale**. Vérifie que `~/.claude/projects/` existe et
contient des fichiers `.jsonl`. Compte-les.
- **Des fichiers** → ✅ la supervision est possible.
- **Rien** → ❌ le pack ne peut rien faire : tout repose sur le fait de savoir où en est une session
  **sans la déranger**.

**b) Lister les autres sessions et leur écrire** — la capacité qui rend le pack **actif**. Sonde-la
vraiment : tente de lister les sessions ouvertes.
- **Tu obtiens une liste** → ✅ le superviseur peut relancer.
- **Les outils n'existent pas ici** → ⚠️ **dégradé, pas mort** : il diagnostique et te dit quoi
  relancer, c'est toi qui relances. Dis-le clairement plutôt que de laisser croire à une panne.

**c) Y a-t-il un parc à superviser ?** Compte les sessions (en t'excluant). **Une seule session, la
tienne** → le pack n'a rien à faire aujourd'hui, et c'est une réponse honnête : il devient utile à
partir de plusieurs chantiers en parallèle.

## 2 — INSTALLER

Rien à installer : pas de dépendance, pas de configuration, pas de script. Le pack est une **méthode**.

Le seul « réglage » utile est un choix de ta part : **où vit la mémoire de ton parc**. Si tu tiens
déjà un tableau de bord de tes chantiers, c'est **lui** — le superviseur y écrit plutôt que dans une
conversation qui disparaîtra. Si tu n'en as pas, ne l'invente pas : la conversation suffit tant que le
parc est petit.

## 3 — EXPLIQUER

**Comment ça marche.** Quand plusieurs sessions tournent, le goulot n'est plus la machine, c'est
**ton attention** : une session qui attend ta réponse reste à l'arrêt indéfiniment. Le superviseur
lit où en est chacune, décide ce qui peut l'être sans toi, relance celles qui dorment, et rend **un**
compte-rendu au lieu de vingt.

Le principe qui gouverne tout le reste : **lire coûte quelques centaines de tokens et ne dérange
personne ; écrire démarre un tour complet** chez la cible. Donc on lit pour savoir, on écrit pour
demander.

**Quand ça se déclenche.** « Supervise mes sessions », « où en sont mes sessions », « relance celles
qui dorment », « j'ai trop de sessions ouvertes » — ou le tour du matin de ce qui a bougé pendant la
nuit.

**Pourquoi ça n'a rien fait.**
1. **Une seule session ouverte** — il n'y a rien à superviser, et c'est normal.
2. **Pas de canal d'écriture** (cas b) → il diagnostique mais ne relance pas. **Ce n'est pas une
   panne**, c'est un mode dégradé qu'il doit annoncer.
3. **Toutes les sessions travaillent** → ne pas déranger est le bon comportement. Un cycle sans
   intervention peut être un bon cycle ; un cycle qui *rapporte* sans que rien n'avance, non.

## Le rapport final

```
Transcripts lisibles : ✅ <n> fichiers | ❌ absent → pack inopérant
Canal d'écriture     : ✅ <n> sessions vues | ⚠️ absent → mode diagnostic seul
Parc à superviser    : <n> session(s) hors la mienne
Écrit sur la machine : rien
```

Puis **une** phrase : ce qu'il peut faire maintenant, ou pourquoi il n'a rien à faire aujourd'hui.
