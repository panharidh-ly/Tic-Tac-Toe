#Partie Etienne
#Fonction de recherche d'index
def index_case_selectioné(valeur,matrice):
    for x, ligne in enumerate(matrice):
        for y,element in enumerate(ligne):
            if element == valeur:
                return (x,y)


if len(liste)== 0:
        print(f"{jaune} Egalité !!!{base}")
        return True

#Affichage travaillé de la grille de jeux:
def grille_de_jeux():
    print("                ")
    print(f"  {vert}Tic{base}{rouge}Tac{base}{jaune}Toe{base}")
    print("+---+---+---+")
    print("| "+monDico[0][0]+" |"+" "+monDico[0][1]+" |"+" "+monDico[0][2]+" |")
    print("+---+---+---+")
    print("| "+monDico[1][0]+" |"+" "+monDico[1][1]+" |"+" "+monDico[1][2]+" |")
    print("+---+---+---+")
    print("| "+monDico[2][0]+" |"+" "+monDico[2][1]+" |"+" "+monDico[2][2]+" |")
    print("+---+---+---+")
  
#Codes couleurs
rouge = "\033[91m"
vert = "\033[92m"
jaune = "\033[93m"
base = "\033[0m"

#Nos listes:
monDico = [["1","2","3"],["4","5","6"],["7","8","9"]]
liste = ["1","2","3","4","5","6","7","8","9"]

grille_de_jeux()

morpion()

#Boucle de redemarage
while True:
    
    monDico = [["1","2","3"],["4","5","6"],["7","8","9"]]
    liste = ["1","2","3","4","5","6","7","8","9"]
    
    demande_relancer_partie=input(f"Nouvelle partie ? ({vert}O{base} ou {rouge}N{base}) :")
    relancer_partie = demande_relancer_partie.upper()
    
    if relancer_partie == "N":
        print("A bientot !")
        break
    elif relancer_partie == "O":
        grille_de_jeux()
        morpion()
    else: 
        print("Je ne vous ai pas compris.")
        continue

print(liste)