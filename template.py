import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "FinanceComplaint"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_validation.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_pusher.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/mango_client.py",
    f"src/{project_name}/config/spark_manager.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/constant/environment.py",
    f"src/{project_name}/data_access/__init__.py",
    f"src/{project_name}/data_access/model_eval_artifact.py",
    f"src/{project_name}/Entity/__init__.py",
    f"src/{project_name}/Entity/artifact_entity.py",
    f"src/{project_name}/Entity/config_entity.py",
    f"src/{project_name}/Entity/metadata_entity.py",
    f"src/{project_name}/Entity/schema.py",
    f"src/{project_name}/ml/__init__.py",
    f"src/{project_name}/ml/estimator.py",
    f"src/{project_name}/ml/feature.py",

    "docker_compose.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "demo.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
        
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w'):
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
