import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project = 'mlprojects'  # Make sure this is correct and consistent

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project}/__init__.py",
    f"src/{project}/components/__init__.py",
    f"src/{project}/components/data_ingestion.py",
    f"src/{project}/components/data_transformation.py",
    f"src/{project}/components/model_trainer.py",
    f"src/{project}/components/model_monitering.py",
    f"src/{project}/pipelines/__init__.py",
    f"src/{project}/pipelines/training_pipeline.py",
    f"src/{project}/pipelines/prediction_pipeline.py",
    f"src/{project}/exception.py",
    f"src/{project}/logger.py",
    f"src/{project}/utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
