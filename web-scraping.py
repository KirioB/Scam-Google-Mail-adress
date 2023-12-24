import requests
import re
import os
import datetime

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# Obtenir la date actuelle au format AAAA-MM-JJ
date_creation = datetime.date.today()

# Formater la date en une chaîne de caractères (par exemple, AAAA-MM-JJ)
format_date = date_creation.strftime("%Y-%m-%d")

# Créer le nom du fichier en utilisant la date formatée
nom_fichier = f"fichier_{format_date}.txt"

# Vérifie si le fichier existe
if os.path.exists(nom_fichier):
    pass
else:
    with open('mon_fichier.txt', 'w') as fichier:
        # Écrire du texte dans le fichier
        fichier.write("Fichier du: "+str(date_creation)+"\n")

 
# Recherche google
query = "usine decoltage vallée arve "
 
for j in search(query, tld="co.in", num=10, stop=50, pause=2):
    print(j)
    #pour chaque URL j on fait une recherche et on sort les numero ou adresse mail
    response=requests.get(j)
    if response.status_code ==200:
        print("reponse positive")
        
    else:
        print('reponse negative avec code derreur :')

    pattern = r'\b[\w\.-]+\[at\][\w\.-]+\.\w+\b|\b[\w\.-]+@[\w\.-]+\.\w+\b|\(0\)\d{2} \d{3} \d{2} \d{2}|0\d{1} \d{2} \d{2} \d{2} \d{2}'
    
    #le pattern recherche les numeros de telephones ainsi que les adresse mail en @ et en [at]
    resultats = re.findall(pattern, response.text)
    for adresse in resultats:
        with open('mon_fichier.txt', 'a') as fichier:
            # Écrire du texte dans le fichier
            fichier.write(j+"\n"+adresse+"\n")

    if resultats == []:
        print("pas dadresse trouvé")