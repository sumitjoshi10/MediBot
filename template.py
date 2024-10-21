import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[$(asctime)s]: %(message)s:')

list_of_file =[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "requirements.txt",
    "app.py",
    "store_index.py",
    "experiment/experiment.ipynb",
    "static/style.css",
    "templates/chat.html"
]

for file_path in list_of_file:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating director {file_dir} for the file {file_name}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path ,"w") as f:
            logging.info(f"Creating empty file {file_path}")
        
    else:
        logging.info(f"{file_name} already exist")
        