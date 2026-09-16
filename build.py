"""
Script de génération statique du portfolio HTML.
Lit data/portfolio.json et injecte les données dans templates/index.html.j2.
"""

import json
from pathlib import Path
import urllib.parse
from jinja2 import Environment, FileSystemLoader

# Dictionnaire de correspondance des badges de stack technique
STACK_BADGES = {
    "Python 3.11": "https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white",
    "Python": "https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white",
    "Docker": "https://img.shields.io/badge/Docker-Multi--stage-2496ED?logo=docker&logoColor=white",
    "Docker (multi-stage)": "https://img.shields.io/badge/Docker-Multi--stage-2496ED?logo=docker&logoColor=white",
    "vLLM": "https://img.shields.io/badge/vLLM-Inference-f18e1f",
    "Qwen3-1.7B-Base": "https://img.shields.io/badge/Qwen3-1.7B-000?logo=alibabacloud&logoColor=white",
    "Qwen3": "https://img.shields.io/badge/Qwen3-1.7B-000?logo=alibabacloud&logoColor=white",
    "FastAPI": "https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white",
    "Gradio": "https://img.shields.io/badge/Gradio-UI-fb7c00",
    "Google Cloud Run": "https://img.shields.io/badge/Cloud_Run-GCP-4285F4?logo=googlecloud&logoColor=white",
    "GCP": "https://img.shields.io/badge/GCP-Cloud_Run-4285F4?logo=googlecloud&logoColor=white",
    "Google Cloud Storage": "https://img.shields.io/badge/Cloud_Storage-GCS-4285F4?logo=googlecloud&logoColor=white",
    "MLflow": "https://img.shields.io/badge/MLflow-0194e2?logo=mlflow&logoColor=white",
    "LightGBM": "https://img.shields.io/badge/LightGBM-Classification-2496ED",
    "FAISS": "https://img.shields.io/badge/FAISS-VectorDB-00599C",
    "Mistral Small": "https://img.shields.io/badge/Mistral-Small-FD6F00",
    "PostgreSQL": "https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white",
    "CI/CD": "https://img.shields.io/badge/CI%2FCD-Cloud_Build-4285F4",
}


def load_portfolio_data(json_path: Path) -> dict:
    """
    @definition : Charge et désérialise le fichier JSON source du portfolio
    @args/params : json_path (Path) : Chemin vers le fichier portfolio.json
    @return : dict : Dictionnaire contenant les données du portfolio
    """
    # Lecture du fichier json structuré
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_skill_badge_url(name: str) -> str:
    """
    @definition : Génère l'URL du badge shields.io pour une compétence via palette déterministe
    @args/params : name (str) : Nom de la compétence / outil
    @return : str : URL du badge shields.io
    """
    # Palette de couleurs déterministe selon la première lettre
    palette = ["3178C6", "5C2D91", "B23A48", "006B3F", "264D8C", "6B4226"]
    color = palette[ord(name[0]) % len(palette)]
    safe_name = urllib.parse.quote(name)
    return f"https://img.shields.io/badge/{safe_name}-{color}?style=flat-square"


def get_stack_badge_url(tech: str) -> str:
    """
    @definition : Retourne l'URL du badge de stack technique avec icône adaptée
    @args/params : tech (str) : Nom de la technologie
    @return : str : URL du badge shields.io
    """
    # Recherche dans le dictionnaire de correspondance des badges de stack
    if tech in STACK_BADGES:
        return STACK_BADGES[tech]
    safe_tech = urllib.parse.quote(tech)
    return f"https://img.shields.io/badge/{safe_tech}-3776AB"


def build_portfolio(
    data_path: Path, template_dir: Path, template_name: str, output_path: Path
) -> None:
    """
    @definition : Génère le fichier index.html final à partir des données JSON et du template Jinja2
    @args/params :
        data_path (Path) : Chemin vers data/portfolio.json
        template_dir (Path) : Répertoire des templates
        template_name (str) : Nom du fichier template Jinja2
        output_path (Path) : Chemin de destination du fichier index.html généré
    @return : None
    """
    # Chargement des données JSON
    data = load_portfolio_data(data_path)

    # Initialisation de l'environnement Jinja2
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # Enregistrement des filtres et fonctions d'aide
    env.filters["skill_badge"] = get_skill_badge_url
    env.filters["stack_badge"] = get_stack_badge_url

    # Récupération et rendu du template
    template = env.get_template(template_name)
    rendered_html = template.render(
        portfolio=data,
        profile=data.get("profile", {}),
        skills=data.get("skills", {}),
        ethics=data.get("ethics", {}),
        projects=data.get("projects", []),
        soft_skills=data.get("soft_skills", []),
        experience=data.get("experience", {}),
        education=data.get("education", []),
        certifications=data.get("certifications", []),
        architecture_diagrams=data.get("architecture_diagrams", {}),
    )

    # Écriture du fichier HTML final
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print(f"✓ Portfolio généré avec succès : {output_path}")


def main() -> None:
    """
    @definition : Point d'entrée principal pour l'exécution du script de build
    @args/params : Aucun
    @return : None
    """
    # Détermination des chemins relatifs au projet
    base_dir = Path(__file__).resolve().parent
    data_file = base_dir / "data" / "portfolio.json"
    templates_dir = base_dir / "templates"
    output_file = base_dir / "index.html"

    # Exécution de la génération
    build_portfolio(
        data_path=data_file,
        template_dir=templates_dir,
        template_name="index.html.j2",
        output_path=output_file,
    )


if __name__ == "__main__":
    main()
