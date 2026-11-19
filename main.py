#1 Afficher_menu_principal
#   options = ["Démarrer le jeu", "Afficher le classement", "Quitter"]
#   retourner Recuperer_choix_utilisateur(options)

#2 Recuperer le Choix utilisateur
#   tant que infini
#      afficher le menu avec les numéros
#           pour chaque option dans enumerate(options, start=1)
#      demander un choix a l'utilisateur
#      si le choix est valide (#3)
#           retourner le choix valide
#      sinon afficher un message d'erreur

#3 Choix_valide
#   si le choix n'est pas un nombre
#      retourner false
#   transformer le choix en nombre entier
#   si le choix est inférieur au minimum ou supérieur au maximum
#      retourner false
#   retourner true

#4. Démarrer le jeu
#4.1 Demander le nom du joueur
#4.2 Créer l'équipe de héros   
#    créer la variable équipe vide
#    tant que l'équipe n'est pas complète 
#       déterminer la liste des personnages disponibles 
#       construire la liste des options à afficher 
#       récupérer le choix utilisateur 
#       ajouter le personnage choisi à l'équipe
#    retourner l'équipe


##4.2.1 Est_equipe_complete(équipe)
#    si la taille de l'équipe est égale à 3
#       retourner true
#    retourner false

#4.2.2 Determiner_personnages_disponibles(liste_personnages_db, équipe)
#    disponibles = liste vide
#    pour chaque personnage dans liste_personnages_db
#       si le personnage n'est pas dans l'équipe
#          ajouter le personnage à disponibles
#    retourner disponibles

#4.2.3 Construire_options_affichables(personnages_disponibles)
#    options = liste vide
#    pour chaque personnage dans personnages_disponibles
#       ajouter "{nom} - {atk} ATK - {def} DEF - {pv} PV" à options
#    retourner options
#
#


#___________________________________________________________________________________________________________________________________________




#4.2.3 Construire_options_affichables(personnages_disponibles)
def construire_aption_affichables(personnages_disponibles):
#    options = liste vide
    option = []
#    pour chaque personnage dans personnages_disponibles
    for personnage in personnages_disponibles:
#       ajouter "{nom} - {atk} ATK - {def} DEF - {pv} PV" à options
#    retourner options



#4.2.2 Determiner_personnages_disponibles(liste_personnages_db, équipe)
def determiner_personnages_disponibles(liste_personnages_db, equipe):
#    disponibles = liste vide
    disponible = []
#    pour chaque personnage dans liste_personnages_db
    for chaque_personnage in liste_personnages_db:
#       si le personnage n'est pas dans l'équipe
        if personnage not in equipe:
#          ajouter le personnage à disponibles
            disponible.append(disponible)
#    retourner disponibles
    return disponible

##4.2.1 Est_equipe_complete(équipe)
def est_equipe_complete(equipe):
#    si la taille de l'équipe est égale à 3
    if len(equipe) == 3:
#       retourner true
        return True
#    retourner false    
    return False


#4.2 Créer l'équipe de héros   
def créer_equipe_héros(liste_personnages_db):
#    créer la variable équipe vide
    equipe = []
#    tant que l'équipe n'est pas complète 
    while not est_equipe_complete(equipe):
#       déterminer la liste des personnages disponibles 
        disponibles = determiner_personnages_disponibles(liste_personnages_db, equipe)
#       construire la liste des options à afficher 
        options = construire_options_affichables(disponibles)
#       récupérer le choix utilisateur 
        choix = recuperer_choix_utilisateur(options)
#       ajouter le personnage choisi à l'équipe
        equipe.append(disponibles[choix - 1])
#    retourner l'équipe
    return equipe


#4.1 Demander le nom du joueur
def demander_nom_joueur():
    while True: 
        nom = input("Entrez voutre nom de joureur : ").strip
        if nom != "":
            return nom
        else:
            print("erreur : le nomne peut pas etre vide")

#4. Démarrer le jeu
def demarrer_le_jeu():
    ...
 
# 3. Vérifier si le choix est valide
def choix_valide(choix, minimum, maximum):
    if not choix.isdigit():
        return False
    choix_entier = int(choix)
    if choix_entier < minimum or choix_entier > maximum:
        return False
    return True

# 2. Récupérer le choix de l'utilisateur
def recuperer_choix_utilisateur(options):
    while True:
        print("\n--- Menu ---")
        for numero, option in enumerate(options, start=1):
            print(f"{numero}. {option}")
        
        choix = input("Votre choix : ")
        
        if choix_valide(choix, 1, len(options)):
            return int(choix)
        else:
            print("Erreur : veuillez entrer un numéro valide.")

# 1. Afficher le menu 
def afficher_menu_principal():
    options = ["Démarrer le jeu", "Afficher le classement", "Quitter"]
    return recuperer_choix_utilisateur(options)

# 0 main
if __name__ == "__main__":
    choix_utilisateur = afficher_menu_principal()
    print(f"Vous avez sélectionné l'option n°{choix_utilisateur}.")
    








































