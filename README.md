# Portfolio — Christophe Mpaga · AI Engineer

[![Build & Sync](https://github.com/AIEngOc2025/Portfolio/actions/workflows/build.yml/badge.svg)](https://github.com/AIEngOc2025/Portfolio/actions/workflows/build.yml)
[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Package Manager](https://img.shields.io/badge/Package_Manager-uv-DE5FE9?logo=astral&logoColor=white)](https://docs.astral.sh/uv/)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub_Pages-222222?logo=githubpages&logoColor=white)](https://aiengoc2025.github.io/Portfolio/)

Portfolio professionnel documentant ma démarche d'**AI Engineer**, centrée sur la conception, l'industrialisation et le passage en production de solutions d'intelligence artificielle fiables, scalables, observables et éthiques.

---

## ✨ À propos

Issu du parcours **AI Engineer** (OpenClassrooms), j'interviens sur l'ensemble de la chaîne de valeur :
- **Cadrage & besoin métier** : analyse d'opportunité, audit de solutions data, planification POC → MVP → PROD, conformité réglementaire (secteurs sensibles et santé).
- **Industrialisation** : architectures conteneurisées modulaires, fine-tuning de LLM open-source, pipelines CI/CD, optimisation GPU.
- **Production & MLOps/AIOps** : déploiement cloud managé (GCP Cloud Run, Vertex AI), observabilité (MLflow), détection de drift, sécurisation (red-teaming) et intégration SIH (HL7/FHIR).

---

## 🚀 Projets mis en avant

| Projet | Description | Stack Technique | Dépôt |
| :--- | :--- | :--- | :--- |
| **🏥 Agent d'accueil hospitalier (CHSA)** | Projet phare : orientation et triage aux urgences pour résorber la surcharge des services hospitaliers. | `Qwen3-1.7B`, `vLLM`, `FastAPI`, `Cloud Run`, `Docker`, `MLflow`, `FHIR` | [agent-triage-hospitalier](https://github.com/AIEngOc2025/agent-triage-hospitalier.git) |
| **🧠 Fine-tuning LLM (Qwen3)** | Fine-tuning et serving d'un LLM. Pivot architectural d'un monolithe vers une architecture modulaire multi-stage découplée. | `vLLM`, `FastAPI`, `Gradio`, `Docker multi-stage`, `GCS`, `Cloud Run` | [agent-triage-hospitalier](https://github.com/AIEngOc2025/agent-triage-hospitalier.git) |
| **📊 Scoring de crédit** | Classification ML pour l'évaluation du risque de crédit bancaire avec validation croisée et API conteneurisée. | `LightGBM`, `Scikit-learn`, `FastAPI`, `Docker`, `GCP` | [MLOps](https://github.com/AIEngOc2025/MLOps.git) |
| **🔍 Système RAG (Événements Parisiens)** | Recherche et question-réponse sur les événements culturels parisiens via bases vectorielles et LLM. | `FAISS`, `Mistral Small`, `FastAPI`, `PostgreSQL` | [RAG](https://github.com/AIEngOc2025/RAG.git) |
| **☁️ MLOps-GCP** | Déploiement automatisé et pipeline CI/CD de modèles ML sur Google Cloud Platform. | `Python`, `Docker`, `GCP Cloud Build`, `Cloud Run` | [MLOps-GCP](https://github.com/AIEngOc2025/MLOps-GCP.git) |

---

## 🛠 Stack Technique

- **Langages & Génération** : Python 3.13+ (géré avec `uv`), Jinja2, HTML5 sémantique, CSS3 (variables, responsive, dark/light mode, feuille de style print ATS-friendly), JavaScript Vanilla.
- **Visualisation & Diagrammes** : [Mermaid.js](https://mermaid.js.org/) pour les architectures dynamiques (modulaire conteneurisée actuelle vs agentique cible LangGraph).
- **MLOps & AIOps** : MLflow, vLLM, Hugging Face Transformers, FAISS, Red-teaming, monitoring de dérive.
- **Data & ML** : PyTorch, TensorFlow / Keras, Scikit-learn, Pandas, NumPy, spaCy.
- **Cloud & DevOps** : Docker (multi-stage), Google Cloud Platform (Cloud Run, GCS, Artifact Registry), GitHub Actions, Git.

---

## 🏗 Architecture du Dépôt

Le portfolio repose sur une architecture **SSG (Static Site Generation)** légère garantissant que les données restent parfaitement synchronisées :

```text
Portfolio/
├── data/
│   └── portfolio.json       # Source unique de vérité (SSOT) : profil, compétences, projets, parcours
├── templates/
│   └── index.html.j2        # Template Jinja2 du site web
├── build.py                 # Script Python de compilation statique (Jinja2 -> index.html)
├── index.html               # Fichier HTML final pré-rendu (100 % autonome, consultable hors-ligne)
├── styles/
│   ├── main.css             # Styles du site (variables, responsive, dark mode)
│   └── print.css            # Feuille de style dédiée à l'impression / PDF / ATS
├── .github/workflows/
│   └── build.yml            # CI/CD : génération et synchronisation automatique lors des pushs
├── pyproject.toml           # Configuration uv et dépendances Python
├── uv.lock                  # Lockfile des dépendances uv
└── .nojekyll                # Désactive le moteur Jekyll sur GitHub Pages
```

---

## ⚙️ Guide d'Utilisation

### 1. Installation des dépendances

Le projet utilise [`uv`](https://docs.astral.sh/uv/) comme gestionnaire d'environnement et de paquets Python :

```bash
uv sync
```

### 2. Mettre à jour et générer le portfolio

Toute modification (nouveau projet, compétence, contact) s'effectue directement dans [`data/portfolio.json`](data/portfolio.json).

Pour compiler et générer le fichier [`index.html`](index.html) :

```bash
uv run python build.py
```

Pour vérifier la conformité du code Python (PEP 8) :

```bash
uv run ruff check build.py
```

### 3. Aperçu local (Preview)

Puisque le HTML est pré-généré statiquement, vous pouvez :
- Soit **double-cliquer** sur `index.html` ou l'ouvrir directement via votre navigateur (protocole `file://`).
- Soit lancer un serveur local :
  ```bash
  python3 -m http.server 8000
  # Ouvrir http://localhost:8000
  ```

---

## 🚀 Déploiement Continu (CI/CD)

Le déploiement est automatisé via **GitHub Pages** et **GitHub Actions** :
1. Chaque push sur la branche `main` modifiant `data/portfolio.json` ou les templates déclenche le workflow `.github/workflows/build.yml`.
2. Le workflow installe `uv`, exécute `build.py` et committe automatiquement le `index.html` à jour si des modifications ont eu lieu.
3. GitHub Pages sert directement les fichiers depuis la racine de la branche `main`.

---

## 🔒 Engagement Éthique & Conformité

- **Protection des données** : Anonymisation native des datasets et conformité RGPD dès la phase POC.
- **Sécurité des LLM** : Intégration de tests automatisés (red-teaming) pour prévenir les risques d'hallucinations et d'injections.
- **Transparence & Auditabilité** : Logs d'audit détaillés, traçabilité des décisions et observabilité rigoureuse en production.

---

## 📬 Contact

- **Email** : [christophempaga@gmail.com](mailto:christophempaga@gmail.com)
- **LinkedIn** : [linkedin.com/in/christopheemilempaga](https://www.linkedin.com/in/christopheemilempaga/)
- **GitHub** : [github.com/AIEngOc2025](https://github.com/AIEngOc2025)

---

## 📄 Licence

Contenu personnel © Christophe Mpaga.
