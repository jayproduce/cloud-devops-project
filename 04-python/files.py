try :
   with open("data.txt", "w") as f:
    f.write("cloud Devops\n")
    f.write("Python file handling\n")
except Exception as e:
    print("Error:", e)

try :
   with open("data.txt", "r") as f:
      content = f.read()
      print(content)
except FileNotFoundError :
   print ("Fichier introuvabe")
