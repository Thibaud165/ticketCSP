import os
import sys

code_max = int(input("\nCode max : "))
avec_prefixe = input("\nAvec prefixe [#-] (o/n) : ")

if avec_prefixe == "o":
    prefixe = "#-"
else:
    prefixe = ""

fichier = "generateur-code/notes.txt"

code_count = 0
code1 = 1
code2 = 0
code3 = 0
code4 = 0
code5 = 0
last_percent = -1

def afficher_progression(pourcent):
    bar_length = 50
    blocks = int((pourcent / 100) * bar_length)
    bar = "█" * blocks + " " * (bar_length - blocks)
    sys.stdout.write(f"\r[{bar}] {pourcent}%")
    sys.stdout.flush()

print("\nRecherche du fichier liste-codes.txt.txt...\n")

if os.path.exists("generateur-code/liste-codes.txt"):
    os.remove("generateur-code/liste-codes.txt")
    print("Fichier trouvé et supprimé\n")
else:
    print("Fichier introuvable\n")

print("Écriture en cours...\n")

while code5 < 10 and code_count < code_max:
    with open("generateur-code/liste-codes.txt", "a") as fichier:
        code = f"{prefixe}{code5}{code4}{code3}{code2}{code1}"
        fichier.write(code + "\n")

    code_count += 1

    percent = int((code_count / code_max) * 100)
    if percent % 1 == 0 and percent != last_percent:
        afficher_progression(percent)
        last_percent = percent

    code1 += 1
    if code1 == 10:
        code1 = 0
        code2 += 1
        if code2 == 10:
            code2 = 0
            code3 += 1
            if code3 == 10:
                code3 = 0
                code4 += 1
                if code4 == 10:
                    code4 = 0
                    code5 += 1


print("")
print(f"\nEcriture de {code_max} codes terminé\n")
