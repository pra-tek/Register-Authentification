
from Enregistrement import enregistrer
from authentification import verifier_credentials
from menu import afficher_menu, sous_menu_hachage, sous_menu_cesar, sous_menu_dataset

# Fonction principale du programme
def main():
    email = input("Entrez votre adresse email : ")
    password = input("Entrez votre mot de passe : ")

    if verifier_credentials(email, password):
        print("Authentification réussie!")
        while True:
            afficher_menu()
            choix = input("Choisissez une option : ").upper()

            if choix == 'A':
                sous_menu_hachage()
                choix_hachage = input("Choisissez une option : ").lower()

                if choix_hachage == 'a':
                    mot = input("Entrez le mot à hacher : ")
                    resultat_hachage = hacher_mot(mot)
                    print("Résultat du hachage : ", resultat_hachage)
                elif choix_hachage == 'b':
                    mot = input("Entrez le mot à attaquer par dictionnaire : ")
                    attaquer_par_dictionnaire(mot)
                elif choix_hachage == 'd':
                    continue

            elif choix == 'B':
                sous_menu_cesar()
                choix_cesar = input("Choisissez une option : ").lower()

                if choix_cesar == 'a':
                    mot = input("Entrez le mot à chiffrer : ")
                    decalage = int(input("Entrez la valeur du décalage : "))
                    mot_chiffre = chiffrer_cesar(mot, decalage)
                    print("Mot chiffré : ", mot_chiffre)
                elif choix_cesar == 'b':
                    mot_chiffre = input("Entrez le mot chiffré : ")
                    decalage = int(input("Entrez la valeur du décalage : "))
                    mot_dechiffre = dechiffrer_cesar(mot_chiffre, decalage)
                    print("Mot déchiffré : ", mot_dechiffre)
                elif choix_cesar == 'c':
                    continue

            elif choix == 'C':
                sous_menu_dataset()
                choix_dataset = input("Choisissez une option : ").lower()

                if choix_dataset == 'a':
                    # Implémentez ici l'affichage du Dataset sous forme de dictionnaire
                    pass
                elif choix_dataset == 'b':
                    # Implémentez ici l'affichage des courbes de votre choix
                    pass
                elif choix_dataset == 'c':
                    continue

            elif choix == 'D':
                print("Au revoir!")
                break
            else:
                print("Option invalide. Veuillez réessayer.")

    else:
        print("Email ou mot de passe incorrect. Veuillez vous enregistrer.")

# Appel de la fonction principale
if __name__ == "__main__":
    main()

