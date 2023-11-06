import hashlib

# Fonction pour vérifier les credentials dans le fichier Enregistrement.txt
def verifier_credentials(email, password):
    with open("Enregistrement.txt", "r") as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            stored_email, stored_password = ligne.strip().split(", ")
            if email == stored_email.split(": ")[1] and password == stored_password.split(": ")[1]:
                return True
        return False

# Fonction pour hacher un mot avec l'algorithme SHA-256
def hacher_mot(mot):
    return hashlib.sha256(mot.encode()).hexdigest()

# Fonction pour attaquer un mot par dictionnaire
def attaquer_par_dictionnaire(mot):
    # Implémentez ici votre propre logique d'attaque par dictionnaire
    pass

# Fonction pour chiffrer un mot par décalage de César
def chiffrer_cesar(mot, decalage):
    resultat = ""
    for char in mot:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            chiffré = chr((ord(char) - ascii_offset + decalage) % 26 + ascii_offset)
            resultat += chiffré
        else:
            resultat += char
    return resultat

# Fonction pour déchiffrer un mot chiffré par César
def dechiffrer_cesar(mot, decalage):
    return chiffrer_cesar(mot, -decalage)

