#1 Afficher le menu (jouer, classement, quitter )
#    Réagir au choix
#    Si le choix est 1 : démarrer le jeu (étape 4)
#    Si le choix est 2 : afficher le classement
#    Si le choix est 3 : afficher « Au revoir » et arrêter le programme
#    Après le jeu ou le classement, revenir à l’étape 1



#2 Recuperer le Choix utilisateur   
#     tant que infini
#       afficher le menu
#       demander un choix a l'utilisateur   

#3. Choix_valide
#   si le choix n'est pas un nombre : afficher "veillez choisir entre 1 et 3"   
#       recommencer
#   transformer le choix en nombre entier
#   si le nombre est entre 1 et 3 que le choix est valide on sort de la répétition
#   sinon afficher "vueillez choisir entre 1 et 3"





#4. Démarrer le jeu
#4.1 Demander le nom du joueur
#4.2 Créer l’équipe de héros
#4.2.1 Partir d’une équipe vide
#4.2.2 Tant que l’équipe a moins de 3 héros :
#    afficher la liste des héros numérotés
#    demander un choix au joueur
#    si le choix est invalide : afficher "une erreur" et recommencer
#    si le héros est déjà dans l’équipe : afficher "Déjà choisi" et recommencer
#    sinon : ajouter le héros à l’équipe
#4.3 Créer l’équipe de monstres 
#4.3.1 Partir d’une équipe vide
#4.3.2 Tant que l’équipe a moins de 3 monstre :
#    afficher la liste des monstre numérotés
#    demander un choix au joueur
#    si le choix est invalide : afficher "une erreur" et recommencer
#    si le monstre est déjà dans l’équipe : afficher "Déjà choisi" et recommencer
#    sinon : ajouter le monstre à l’équipe
#4.4 Lancer le combat

#5 regle de combat 
#5.1

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






   


# 3 Choix_valide
def choix_valide(choix):
    # si le choix n'est pas un nombre : afficher "veuillez choisir entre 1 et 3"
    if not choix.isdigit():
        print("Veuillez choisir entre 1 et 3")
        return None  # Indique que le choix n'est pas valide (il faudra recommencer)

    # transformer le choix en nombre entier
    choix = int(choix)

    # si le nombre est entre 1 et 3, le choix est valide
    if 1 <= choix <= 3:
        return choix  # Renvoie le nombre validé
    # sinon afficher "veuillez choisir entre 1 et 3"
    else:
        print("Veuillez choisir entre 1 et 3")
        return None

# 2 Recuperer le Choix utilisateur
def recuperer_choix():
    # tant que infini
    while True:
        # afficher le menu
        afficher_menu()
        # demander un choix a l'utilisateur
        saisie = input("Votre choix (1-3) : ").strip()

        # On vérifie avec l'étape 3
        resultat = choix_valide(saisie)

        # Si le choix est valide (différent de None), on sort de la répétition
        if resultat is not None:
            return resultat

# 1 Afficher le menu (jouer, classement, quitter)
def afficher_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Jouer")
    print("2. Classement")
    print("3. Quitter")
    print("======================")

# Programme principal
def main():
    choix = recuperer_choix()
    print(f"Action validée : option {choix}")

if __name__ == "__main__":
    main()







































