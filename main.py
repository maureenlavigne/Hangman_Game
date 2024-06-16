# Prérequis principaux : conditions, boucles et chaines de caractères
# Difficulté : Moyenne
# https://lesbricodeurs.fr/articles/jeu-du-pendu-python/

import time

# Functions
def slow_writing(txt, speed=0.05):
    for c in txt:
        print(c, end="")
        time.sleep(speed)
    print()

# Welcome user
slow_writing("Bienvenue dans le jeu du pendu.")
time.sleep(2)
slow_writing("Je vais choisir un mot que tu vas devoir deviner.")
time.sleep(3)

# Computer chooses word (simple version with 1 solution)
solution = "casserole"
slow_writing("C'est bon. A toi de jouer !")
time.sleep(2)

# Rules : poser la variable des tentatives.
# Lorsque la variable tentatives atteint 0, le joueur perd la partie.
tentatives = 10
slow_writing("Attention, tu n'as le droit qu'à 10 erreurs.")
slow_writing("Chaque erreur rapproche ton pendu de la potence.")

# Configurer l'affichage des lettres manquantes.
affichage = ""
for letter in solution: # pour chaque lettre dans le mot à trouver/la solution
  affichage = affichage + "_ "

# Garder une liste des lettres qui ont été découvertes, pour pouvoir mettre à jour l’affichage
lettres_trouvees = ""

# Start of game, user write a letter
while tentatives>0:
    print("Mot à deviner : ", affichage)
    proposition = input("Propose une lettre : ")

    # Ensuite, il y a deux possibilités
    # Si la proposition est une lettre contenue dans la solution, alors il faut l’ajouter à la liste des lettres trouvées.
    # Sinon le joueur perd une tentative.

    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("-> Bravo ! Le mot était bien " + solution + ".")
    else:
        tentatives = tentatives - 1
        print("-> Raté. Il te reste", tentatives, "tentatives")
        # Optionnel : dessiner le pendu.
        if tentatives == 0:
            print(" ==========Y= ")
        if tentatives <= 1:
            print(" ||/       |  ")
        if tentatives <= 2:
            print(" ||        0  ")
        if tentatives <= 3:
            print(" ||       /|\ ")
        if tentatives <= 4:
            print(" ||       /|  ")
        if tentatives <= 5:
            print("/||           ")
        if tentatives <= 6:
            print("==============\n")

    # Mettre à jour l'affichage du mot.
    affichage = "" # effacer ce que contenait la variable affichage
    for letter in solution: # pour chaque lettre de la solution, regarder si elle fait partie des lettres trouvées
        if letter in lettres_trouvees:
            affichage += letter + " "
        else:
            affichage += "_ "
    # évaluer si il reste des lettres à découvrir
    if "_" not in affichage:
        print(">>> Gagné! <<<")
        break

print("    * Fin de la partie *    ")
