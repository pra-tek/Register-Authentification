
# Fonction principale pour le menu
def afficher_menu():
    print("Menu principal :")
    print("A- Donnez un mot à hacher")
    print("B- Décalage par César")
    print("C- Collecter une Dataset de votre choix")
    print("D- Quitter")

# Fonction pour afficher le sous-menu du choix A du menu principal
def sous_menu_hachage():
    print("Menu de hachage :")
    print("a- Hacher le mot par SHA-256")
    print("b- Attaquer par dictionnaire le mot inséré")
    print("d- Revenir au menu principal")

# Fonction pour afficher le sous-menu du choix B du menu principal
def sous_menu_cesar():
    print("Menu de décalage par César :")
    print("a- Donnez un mot à chiffrer")
    print("b- Chiffrer le message")
    print("c- Déchiffrer le message")
    print("d- Revenir au menu principal")

# Fonction pour afficher le sous-menu du choix C du menu principal
def sous_menu_dataset():
    print("Menu de Dataset :")
    print("a- Afficher le Dataset sous forme de dictionnaire")
    print("b- Afficher des courbes de votre choix")
    print("c- Revenir au menu principal")

