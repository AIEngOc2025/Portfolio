# Portfolio — Christophe Mpaga · AI Engineer

Site statique présentant le portfolio AI Engineer (projets, compétences, parcours, contact).

## ✨ Aperçu

Site monopage en HTML/CSS/JS pur, sans build :

- **Sections** : Hero · À propos · Compétences · Projets (CHSA, fine-tuning LLM, additionnels) · Savoir-être · Parcours & Formation · Contact
- **Visuels** : diagrammes Mermaid (architecture livrée + cible agentique) et badges `shields.io`
- **Thème** : clair / sombre / automatique (selon `prefers-color-scheme`)
- **Responsive** : mobile → tablette → desktop
- **Imprimable** : `Ctrl+P` → version ATS-friendly (`styles/print.css`)

## 🚀 Preview local

Le site utilise un `fetch()` pour charger `data/portfolio.json`, donc il faut le servir via HTTP (pas en `file://`) :

```bash
cd /Users/mpaga/OC/Portfolio
python3 -m http.server 8000
# Ouvrir http://localhost:8000 dans le navigateur
```

## 🌍 Déploiement sur GitHub Pages

1. Pousser le dossier sur un repo GitHub
2. Settings → Pages → Source : `Deploy from a branch` → `main` / `root`
3. Le site sera disponible à `https://<user>.github.io/<repo>/`

Le fichier `.nojekyll` est présent pour désactiver le traitement Jekyll (utile pour les chemins en `.css`/`.json`).

## 📝 Données à compléter

Tous les champs marqués `TODO_USER` dans `data/portfolio.json` doivent être renseignés avant publication :

- Coordonnées : email, username GitHub, URL LinkedIn
- Liens précis des dépôts GitHub pour chaque projet
- Localisation précise et disponibilité
- Niveaux réels de compétence par outil (au-delà de l'estimation actuelle)
- Années d'expérience par poste d'enseignement
- Diplômes antérieurs (établissement, intitulé exact, année)
- Certifications éventuelles (GCP, AWS, Kubernetes, etc.)

Une fois le JSON mis à jour, ces valeurs se reflètent dans la grille de compétences (script d'injection dans `index.html`) et la section Contact (mise à jour manuelle des attributs `href` + texte si nécessaire).

## 🗂 Structure du projet

```
.
├── index.html                 Page principale
├── styles/
│   ├── main.css               Charte graphique + responsive + dark mode
│   └── print.css              Version imprimable (Ctrl+P / PDF)
├── data/
│   └── portfolio.json         Source de données structurée (skills, projets, etc.)
├── assets/                    Dossier prévu pour exports statiques (badges, diagrams)
├── .nojekyll                  Désactive Jekyll sur GitHub Pages
└── README.md                  Ce fichier
```

## 🧰 Stack du portfolio

- HTML5 sémantique
- CSS3 (variables CSS, Grid, Flexbox, `prefers-color-scheme`, `color-mix`)
- JavaScript vanilla (aucune dépendance npm)
- [Mermaid 10](https://mermaid.js.org/) via CDN (rendu client-side)
- [shields.io](https://shields.io/) via CDN (badges de stack)
- Police [Inter](https://rsms.me/inter/) via Google Fonts

## ♿ Accessibilité

- Navigation clavier (Tab) sur tous les liens/boutons
- Skip-link "Aller au contenu"
- Contraste AA (palette vérifiée)
- Attributs `aria-label` sur navigation, tableaux et boutons iconiques
- `lang="fr"` sur `<html>`
- Sémantique : `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`

## 📄 Licence

Contenu personnel © Christophe Mpaga. Code libre pour adaptation pédagogique.
