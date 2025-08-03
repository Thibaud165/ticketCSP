import csv
import os

print("\nRecherche du fichier liste-div.txt...\n")

if os.path.exists("generateur-code/liste-div.txt"):
    os.remove("generateur-code/liste-div.txt")
    print("Fichier trouvé et supprimé\n")
else:
    print("Fichier introuvable\n")

print("Écriture en cours...\n")

with open(".\.\codes.csv", mode="r", newline='', encoding="utf-8") as f:
    lignes = list(csv.reader(f))

utilisation = ""
entete = lignes[0]
index_nom = entete.index("nom")
index_prenom = entete.index("prenom")
index_categorie = entete.index("categorie")
index_code = entete.index("code-complet")
index_utiliser = entete.index("utiliser")

for i in range(1, len(lignes)):

    ligne = lignes[i]
    nom = ligne[index_nom].strip()
    prenom = ligne[index_prenom].strip()
    categorie = ligne[index_categorie].strip()
    code = ligne[index_code].strip()
    utiliser = ligne[index_utiliser].strip()
    

    if utiliser == "oui":
        utilisation = "Utilisé"
    elif utiliser == "non":
        utilisation = "Inutilisé"

    div = f'<div class="case {nom.lower()}{prenom.upper()}"><p class="prenom">{prenom}</p><p class="nom">{nom}</p><p class="code">{code}</p><p class="inutilisé">{utilisation}<p>'

    with open("generateur-code\liste-div.txt", mode="a", newline='', encoding="utf-8") as f:
        f.write(div + "\n")

print("HTML ecrit avec succes")