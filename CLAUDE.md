# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Vue d'ensemble

Portfolio monopage statique généré via un script Python Jinja2 (`build.py`) présentant le profil AI Engineer de Christophe Mpaga. Les données sont entièrement centralisées dans `data/portfolio.json` (Single Source of Truth), et le rendu statique est généré dans `index.html` via le template `templates/index.html.j2`.

Sections : Hero · À propos · Compétences · Projets (CHSA, fine-tuning LLM, additionnels) · Savoir-être · Parcours & Formation · Engagement Éthique · Contact.

## Commandes utiles

### Générer le site (synchronisation)

```bash
uv run python build.py
```

### Preview local

Ouvrir directement `index.html` dans un navigateur (fonctionne nativement en `file://`), ou via serveur local :

```bash
python3 -m http.server 8000
# Ouvrir http://localhost:8000
```

### Déploiement & Automatisation

Push sur la branche `main` d'un dépôt GitHub.
- Le workflow GitHub Actions `.github/workflows/build.yml` s'exécute lors de toute modification sur `data/portfolio.json` ou les templates et met à jour `index.html`.
- Déploiement automatique sur GitHub Pages (Settings → Pages → Source : `Deploy from a branch` → `main` / `root`).
- Le fichier `.nojekyll` à la racine désactive Jekyll (nécessaire pour les chemins en `.css`/`.json`).

## Architecture du code

```
build.py                Script de génération statique (Jinja2)
templates/
  index.html.j2         Template HTML Jinja2 du portfolio
index.html              Fichier HTML statique généré
styles/
  main.css              Charte graphique (variables CSS), responsive, dark mode (toggle + prefers-color-scheme)
  print.css             Version imprimable / PDF (Ctrl+P) — ATS-friendly, chargée via media="print"
data/
  portfolio.json        Source unique de vérité : profil, compétences (5 piliers), projets, parcours, éthique
.github/workflows/
  build.yml             CI/CD de synchronisation automatique de index.html
assets/
  badges/, diagrams/    Dossiers prévus pour exports statiques
.nojekyll               Désactive Jekyll sur GitHub Pages
```

### Points d'attention structurels

- **`data/portfolio.json` est l'unique source de vérité** pour : `profile`, `skills`, `ethics`, `projects`, `experience`, `soft_skills`, `education`, `certifications`, `architecture_diagrams`.
- Toute modification doit être faite dans `data/portfolio.json`, puis répercutée dans `index.html` via `uv run python build.py` (ou automatiquement par la CI GitHub Actions).
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
