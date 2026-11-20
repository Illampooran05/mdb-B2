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


#4.2.1 Est_equipe_complete(équipe)
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
# 4.3 Créer l'équipe de monstres(liste_monstres_db)
#    créer la variable equipe vide
#    tant que l'équipe n'est pas complète 
#       déterminer la liste des monstres disponibles 
#       choisir un monstre au hasard dans les disponibles
#       ajouter le monstre choisi à l'équipe
#    retourner l'équipe


# Affrontement contre des monstres en boucle jusqu'à la défaite.
#combat_a_mort 
#   recuperer les duex équipe (créer_equipe_héros, créer_equipe_monstre)
#   tent que equipe monstre en vie et equipe hero en vie
#      equipe hero attaquent le monstre 
#          Pour chaque atk heros     
#             monstre perde des pv 
#          si les pv du equipe_monstre == 0 == Victoire 
#      
#      equipe monstre atk un héro à harasard    
#              reduit le pv un heros 
#          si les pv equipe_heros == 0 == fin de la partie   


#       
#      
#         
#  
#      





#___________________________________________________________________________________________________________________________________________
import random
from models import list_monstre, list_personnages






#4.2.3 Construire_options_affichables(personnages_disponibles)
def construire_options_affichables(personnages_disponibles):
#    options = liste vide
    option = []
#    pour chaque personnage dans personnages_disponibles
    for personnage in personnages_disponibles:
#       ajouter "{nom} - {atk} ATK - {def} DEF - {pv} PV" à options
        option.append(f"{personnage['nom']} - {personnage['atk']} ATK - {personnage['def']} DEF - {personnage['pv']} PV ")
#    retourner options
    return option


#4.2.2 Determiner_personnages_disponibles(liste_personnages_db, équipe)
def determiner_personnages_disponibles(liste_personnages_db, equipe):
#    disponibles = liste vide
    disponible = []
#    pour chaque personnage dans liste_personnages_db
    for chaque_personnage in liste_personnages_db:
#       si le personnage n'est pas dans l'équipe
        if list_personnages not in equipe:
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


# 4.3 Créer l'équipe de monstres(liste_monstres_db)
def creer_equipe_monstres(liste_monstre_db):
#    créer la variable equipe vide
    equipe = []
#    tant que l'équipe n'est pas complète
    while not est_equipe_complete(equipe):
#       déterminer la liste des monstres disponibles 
        disponibles = determiner_personnages_disponibles(liste_monstre_db, equipe)
#       choisir un monstre au hasard dans les disponibles
        monstre_choisi = random.choice(disponibles)
#       ajouter le monstre choisi à l'équipe
        equipe.append(monstre_choisi.copy())
#    retourner l'équipe
    return equipe
  
#4.2 Créer l'équipe de héros   
def créer_equipe_héros(liste_personnage_db):
#    créer la variable équipe vide
    equipe = []
#    tant que l'équipe n'est pas complète 
    while not est_equipe_complete(equipe):
#       déterminer la liste des personnages disponibles 
        disponibles = determiner_personnages_disponibles(liste_personnage_db, equipe)
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
    while True:
        choix_utilisateur = afficher_menu_principal()
        
        if choix_utilisateur == 1:
            demarrer_le_jeu(list_personnages, list_monstre)
        elif choix_utilisateur == 2:
            print("\nAffichage du classement...")
        elif choix_utilisateur == 3:
            print("\nAu revoir !")
            break









































