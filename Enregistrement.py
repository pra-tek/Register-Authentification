import re

# Fonction pour vérifier si l'email est valide
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Fonction pour vérifier si le mot de passe est valide
def is_valid_password(pwd):
    pwd_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pwd_regex, pwd)

# Fonction principale pour l'enregistrement
def enregistrer():
    email = input("Entrez votre adresse email: ")
    password = input("Entrez votre mot de passe: ")

    # Vérification de l'email et du mot de passe
    if is_valid_email(email) and is_valid_password(password):
        # Enregistrement dans le fichier Enregistrement.txt
        with open("Enregistrement.txt", "a") as fichier:
            fichier.write(f"Email: {email}, Mot de passe: {password}\n")
        print("Enregistrement réussi!")
    else:
        print("Email ou mot de passe invalide. Veuillez réessayer.")

# Appel de la fonction d'enregistrement
enregistrer()

