import os 
from datetime import datetime 

date = datetime.now()

current_dir = os.getcwd()
 
if not os.path.exists("backup"):
   os.mkdir("backup")

with open("backup.txt", "w") as f:
    f.write("la date est : \n")
    f.write("le dossier courant est :\n")

    print("la date est :", date)
    print("le dossier courant est :", current_dir)

