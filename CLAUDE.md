# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Vue d'ensemble

Portfolio monopage statique (HTML/CSS/JS pur, **aucune étape de build ni gestionnaire de paquets**) présentant le profil AI Engineer de Christophe Mpaga. Le site charge du contenu dynamique depuis `data/portfolio.json` via `fetch()`, ce qui impose un serveur HTTP local — `file://` ne fonctionne pas.

Sections : Hero · À propos · Compétences · Projets (CHSA, fine-tuning LLM, additionnels) · Savoir-être · Parcours & Formation · Contact.

## Commandes utiles

### Preview local

```bash
cd /Users/mpaga/OC/Portfolio
python3 -m http.server 8000
# Ouvrir http://localhost:8000
```

### Déploiement

Push sur la branche `main` d'un dépôt GitHub, puis Settings → Pages → Source : `Deploy from a branch` → `main` / `root`. Le fichier `.nojekyll` à la racine désactive Jekyll (nécessaire pour les chemins en `.css`/`.json`).

Il n'existe **aucune** commande de build, lint, format, ou test — tout est statique. Pour valider une modification, ouvrir la page dans le navigateur et inspecter visuellement / via DevTools.

## Architecture du code

```
index.html              Structure + 4 blocs JS inline (année, thème, compétences, copier-email)
styles/
  main.css              Charte graphique (variables CSS), responsive, dark mode (toggle + prefers-color-scheme)
  print.css             Version imprimable / PDF (Ctrl+P) — ATS-friendly, chargée via media="print"
data/
  portfolio.json        Source de données structurée : profil, compétences (5 piliers), projets, parcours
assets/
  badges/, diagrams/    Dossiers prévus pour exports statiques (actuellement vides)
.nojekyll               Désactive Jekyll sur GitHub Pages
```

### Points d'attention structurels

- **`data/portfolio.json` est la source de vérité** pour : `profile`, `skills` (5 piliers : `devops`, `mlops`, `aiops`, `cloudops`, `data_ml`), `projects`, `experience`, `soft_skills`, `education`, `certifications`, `architecture_diagrams`. Tout champ marqué `TODO_USER` doit être renseigné avant publication.
- Le rendu des compétences (section Skills) est fait par JS : `fetch("data/portfolio.json")` → injection dans `#skillsGrid` et `#dataMlSkills`. Un fallback embarqué gère le cas `file://` en injectant un bandeau d'avertissement.
- Les sections Projets (CHSA, fine-tuning, additionnels), Savoir-être, Formation et Contact sont **écrites en dur dans `index.html`** — la modification des URLs GitHub/LinkedIn/email se fait à la fois dans `data/portfolio.json` ET dans les attributs `href` des cartes Contact de `index.html`.
- Les diagrammes d'architecture sont des blocs `<pre class="mermaid">` rendus par Mermaid 10 (CDN). Le thème Mermaid est ré-initialisé après chaque toggle de thème clair/sombre.
- Le toggle de thème utilise `localStorage` (clé `portfolio-theme`) avec valeur `light`/`dark`, sinon suit `prefers-color-scheme`.
- Les badges de stack sont des images `shields.io` (CDN) ; les badges de compétences sont générés dynamiquement par la fonction `badge(name)` dans le JS inline (palette déterministe basée sur `charCodeAt(0)`).
- **Pas de framework JS, pas de bundler, pas de TypeScript, pas de tests automatisés.**

## Stack

- HTML5 sémantique (`lang="fr"`, `<header>`/`<nav>`/`<main>`/`<section>`/`<article>`/`<footer>`, `aria-label`, skip-link)
- CSS3 (variables CSS, Grid, Flexbox, `prefers-color-scheme`, `color-mix`)
- JavaScript vanilla (aucune dépendance npm)
- Mermaid 10 via CDN (diagrammes)
- shields.io via CDN (badges de stack)
- Inter via Google Fonts

## Accessibilité (déjà en place)

Contraste AA, navigation clavier, skip-link "Aller au contenu", `aria-label` sur navigation/tableaux/boutons iconiques, sémantique HTML5.

## Travail futur typique

- Compléter les `TODO_USER` dans `data/portfolio.json` (email, GitHub username, LinkedIn, années d'expérience, diplômes antérieurs, certifications).
- Après mise à jour du JSON, mettre à jour manuellement les `href` des cartes GitHub/LinkedIn de la section Contact dans `index.html` (le JS ne touche pas ces liens).
- Pour ajouter une compétence : éditer le tableau `tools` du pilier concerné dans `data/portfolio.json` — le rendu JS s'adapte automatiquement.
