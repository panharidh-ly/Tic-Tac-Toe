#Fonction déterminant les conditions de victoire
def choix_victoire(joueur):
    
    for ligne in monDico:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            print(f"{joueur},{jaune}vous avez gagné !! l'autre joueur paye l'apero.{base} ")
            return True
    
    for colonne in range(3):
        if monDico[0][colonne] == monDico[1][colonne] == monDico[2][colonne] and monDico[0][colonne] != " ":
            print(f"{joueur},{jaune}vous avez gagné !! l'autre joueur paye l'apero. {base}")
            return True
        
    if (monDico[0][0] == monDico[1][1] == monDico[2][2] and monDico[0][0] != " ") or (monDico[0][2] == monDico[1][1] == monDico[2][0] and monDico[0][2] != " "):
        print(f"{joueur},{jaune}vous avez gagné !! l'autre joueur paye l'apero. {base}")
        return True
    
    if len(liste)== 0:
        print(f"{jaune} Egalité !!!{base}")
        return True