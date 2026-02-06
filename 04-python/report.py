import os
from datetime import datetime 

date = datetime.now()

current_dir = os.getcwd()

files = os.listdir(current_dir)
number_of_files = len(files)
 
if not os.path.exists("report"):
    os.mkdir("report")

with open("report/system_report.txt", "w") as f:
    f.write("la date est :{date}\n")
    f.write("le chemi dossier courant est : {current_dir} \n")
    f.write("le nombre de fichiers présents dans le dossier courant est :{number_of_files} \n")

    print("Rapport généré avec succès")
    print("la date est :", date)
    print("le chemi dossier courant est :", current_dir)
    print("le nombre de fichiers présents dans le dossier courant est :", number_of_files)

