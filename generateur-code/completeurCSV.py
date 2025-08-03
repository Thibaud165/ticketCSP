import csv

# U7 U9 U11 U13 U15 U18 Senior Loisir Dirigant
liste_vetement = ["Reversible", "Reversible", "Reversible", "Maillot-Short", "Maillot-Short", "Pull", "Pull", "Chasuble", "T-shirt"]

fichier = ".\.\codes.csv"

with open(fichier, mode="r", newline='', encoding="utf-8") as f:
    lignes = list(csv.reader(f))

entetes = lignes[0]
index_nom = entetes.index("nom")
index_prenom = entetes.index("prenom")
index_categorie = entetes.index("categorie")
index_code = entetes.index("code")
index_code_complet = entetes.index("code-complet")

for i in range(1, len(lignes)):
    ligne = lignes[i]
    nom = ligne[index_nom].strip()
    prenom = ligne[index_prenom].strip()
    categorie = ligne[index_categorie].strip()
    code = ligne[index_code].strip()

    if not nom or not prenom or not code:
        break
    
    if categorie == "U7":
        vetement = liste_vetement[0]
    elif categorie == "U9":
        vetement = liste_vetement[1]
    elif categorie == "U11":
        vetement = liste_vetement[2]
    elif categorie == "U13":
        vetement = liste_vetement[3]
    elif categorie == "U15":
        vetement = liste_vetement[4]
    elif categorie == "U18":
        vetement = liste_vetement[5]
    elif categorie == "Senior":
        vetement = liste_vetement[6]
    elif categorie == "Loisir":
        vetement = liste_vetement[7]
    elif categorie == "Dirigant":
        vetement = liste_vetement[8]

    prenom_nom = prenom.lower() + prenom.upper()
    ligne[index_code_complet] = f"#{code}-{prenom_nom}-{categorie}-{vetement}"

# Écrire le fichier mis à jour
with open(fichier, mode="w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(lignes)

print("Code-complet mis à jour dans le fichier.")
