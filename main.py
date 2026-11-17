1#  Afficher le menu (jouer, classement, quitter )

2# Recuperer le Choix utilisateur   
#     tant que infini
#       afficher le menu
#       demander un choix a l'utilisateur   
#       si le choix n'est pas un nombre : afficher "veillez choisir entre 1 et 3" et recommencer
#       transformer le choix en nombre entier
#       si le nombre est entre 1 et 3 que le choix est valide on sort de la répétition
#       sinon afficher "vueillez choisir entre 1 et 3"  


#3#démarrer le jeu
#3.1demander le nom d' utilisateur
#3.2 créations équipe hero
# choisir 3 héros 
#3.3 créations équipe monstre
# choisir 3 monstre 
#3.4 lancer le combat
# gère la logique du combat
# Lancer les vagues de combat
#terminer les combats et stocker le score






#_____________________________________________________________________________________________________________________________________________________________
  # Afficher le menu
  # Recuperer un valide parmi les option
  #    tant que infini
  #         afficher les options numerotees
  #             pour chaque option dans enumerate(options, start=1) 
  #                 afficher {i}. option
  #         demander un choix a l'utilisateur
  #         si le choix est valide
  #             retourner le choix valide 
  #         afficher un message d'erreur

# choix valide 
#    si le choix n'est pas isaigit( )
#       retourner false
#    convertir le choix en entier
#    si el choix est inférieur au minimum ou supérieur au maximum   
#       retourner false
#    retourner true
#___________________________________________________________________________________________________________________________________________________________________________________________________





def afficher_menu():
    print("=== MENU PRINCIPAL ===")
    print("1. Jouer")
    print("2. Classement")
    print("3. Quitter")
    print("======================")

def main():
    # Recuperer le Choix utilisateur
    # tant que infini
    while True:
        # afficher le menu
        afficher_menu()
        
        # demander un choix a l'utilisateur
        choix = input("Votre choix (1-3) : ").strip()
        
        # si le choix n'est pas un nombre : afficher "veuillez choisir entre 1 et 3" et recommencer
        if not choix.isdigit():
            print("Veuillez choisir entre 1 et 3")
            continue
            
        # transformer le choix en nombre entier
        choix = int(choix)
        
        # si le nombre est entre 1 et 3, le choix est valide, on sort de la répétition
        if 1 <= choix <= 3:
            break
        # sinon afficher "veuillez choisir entre 1 et 3"
        else:
            print("Veuillez choisir entre 1 et 3")

    # Suite du programme une fois que le choix est valide
    if choix == 1:
        print("Lancement de la partie...")
    elif choix == 2:
        print("Affichage du classement...")
    elif choix == 3:
        print("Au revoir !")

if __name__ == "__main__":
    main()

  




