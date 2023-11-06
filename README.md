# Register-Authentification


Descriptipion des fichiers

## Enregistrement

Enregistrement des informations d'authentification dans un fichier nommé "Enregistrement.txt", à savoir :
  - l'adresse email
      Avant d'être l'enregistrer, nous devons verifier la valider de l'email fournir par l'utilisateur au travers des Regex
  - le mot de passe
      Le mot de passe doit non seulement être saisi par l'utilisateur et ne pas s'afficher à l'écran, mais aussi respecter des règles préétabli tel que:
        * longueur de 8
        * majuscule
        * minuscule
        * chiffre

## Authentification

Comparaison de l'email et du pwd saisir par l'utilisateur avec ceux enregistrer dans le fichier "Enregistrement.txt".
Si les credentials existent dans "Enregistrement.txt", un menu s'affichera sinon il est amené à s'enregistrer.

## Menu

Une fois authentifié, le menu apparait, subdiviser en 03 partie :
  - Donnez un mot à haché (en mode invisible)
  - Décalage par CESAR
  - Collecter une Dataset de votre choix 

## Main

Ce fichier contient les appels des autres fichiers, ainsi que le code principal du projet.
