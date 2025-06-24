import os
from pathlib import Path

source_folder = 'src' # the main folder having all the components/code files/local packages

list_of_files = [
    f"{source_folder}/__init__.py",
    f"{source_folder}/components/__init__.py",
    f"{source_folder}/components/data_ingestion.py",  
    f"{source_folder}/components/data_validation.py",
    f"{source_folder}/components/data_transformation.py",
    f"{source_folder}/components/model_trainer.py",
    f"{source_folder}/components/model_evaluation.py",
    f"{source_folder}/components/model_pusher.py",
    f"{source_folder}/configuration/__init__.py",
    f"{source_folder}/configuration/mongo_db_connection.py",
    f"{source_folder}/configuration/aws_connection.py",
    f"{source_folder}/cloud_storage/__init__.py",
    f"{source_folder}/cloud_storage/aws_storage.py",
    f"{source_folder}/data_access/__init__.py",
    f"{source_folder}/data_access/proj1_data.py",
    f"{source_folder}/constants/__init__.py",
    f"{source_folder}/entity/__init__.py",
    f"{source_folder}/entity/config_entity.py",
    f"{source_folder}/entity/artifact_entity.py",
    f"{source_folder}/entity/estimator.py",
    f"{source_folder}/entity/s3_estimator.py",
    f"{source_folder}/exception/__init__.py",
    f"{source_folder}/logger/__init__.py",
    f"{source_folder}/pipline/__init__.py",
    f"{source_folder}/pipline/training_pipeline.py",
    f"{source_folder}/pipline/prediction_pipeline.py",
    f"{source_folder}/utils/__init__.py",
    f"{source_folder}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")