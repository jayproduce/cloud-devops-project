import os 
from datetime import datetime

print("le dossier courant :", os.getcwd())
print("la liste des fichiers du dossier :", os.listdir())

if not os.path.exists("logs"):
    os.mkdir("logs")

log_file = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"


with open(log_file, "w") as f:
    f.write("le script a bien été exécuté\n")
    
print("log créé :", log_file)
    