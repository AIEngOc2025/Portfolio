# Portfolio — Christophe Mpaga · AI Engineer

Site statique présentant mon parcours et mes projets en tant qu'AI Engineer.

## ✨ À propos

Ce portfolio documente ma démarche d'ingénieurie IA, centrée sur l'industrialisation de solutions fiables et scalables en production. Vous y trouverez mes projets techniques, ma maîtrise des enjeux MLOps/DevOps/AIOps, ainsi que mon engagement éthique.

## 🚀 Projets mis en avant

- **🏥 Agent d'accueil hospitalier (CHSA)** : Projet phare d'industrialisation (cadrage POC → PROD, architecture modulaire).
- **🧠 Fine-tuning LLM (Qwen3)** : Déploiement multi-stage sur Cloud Run.
- **📊 Scoring de crédit** : Classification ML (LightGBM) avec exposition API.
- **🔍 Système RAG** : Recherche d'événements culturels (FAISS, Mistral Small).

## 🛠 Stack Technique

- **Langages** : Python 3.11, JavaScript (Vanilla), HTML5, CSS3.
- **MLOps/AIOps** : MLflow, vLLM, LangGraph (prévu), Red-teaming.
- **Infrastructure & DevOps** : Docker (Multi-stage), GCP (Cloud Run, GCS), CI/CD (GitHub Actions/Cloud Build).

## ⚙️ Prérequis & Utilisation

### Preview local
Ce site charge dynamiquement les données depuis `data/portfolio.json`. Pour le visualiser localement, utilisez un serveur HTTP :

```bash
python3 -m http.server 8000
# Puis ouvrez http://localhost:8000
```

### Déploiement
Le projet est configuré pour GitHub Pages via le déploiement direct depuis la branche `main` (fichier `.nojekyll` présent).

## 📄 Licence
Contenu personnel © Christophe Mpaga.
