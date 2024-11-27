#Fonction pour les tours de jeu
def tour (joueur,symbole):
    
    while True:  
        
        choix_case = input(f"{joueur} donne un numéro de case : ")
        
        if choix_case not in liste:
            print("La valeur renseignée n'est pas valide, essaie encore.")
            continue  
        
        clef, valeur = index_case_selectioné(choix_case,monDico)
        monDico[clef][valeur] = symbole

#impression de liste myDico modifée
        grille_de_jeux()
        
        liste.remove(choix_case)
        
        return choix_victoire(joueur)

#Fonction de jeux
def morpion():
    try:
        while True:

            if tour(f"{rouge}Joueur 1 : X{base}", f"{rouge}X{base}"):
                break
            if tour(f"{vert}Joueur 2 : O{base}", f"{vert}O{base}"):
                break
    except KeyboardInterrupt:
        exit()