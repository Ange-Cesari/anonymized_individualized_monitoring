# GenerateJSON.py


## Introduction
Le script fourni est un programme Python qui génère des fichiers JSON avec des données aléatoires. Chaque fichier contient les données pour une entrée, y compris l'individu, les coordonnées x, y et z, ainsi que le temps. Le programme génère un nom de fichier aléatoire de 5 lettres pour chaque fichier JSON.

## Bibliothèques
Le programme utilise les bibliothèques suivantes :
- json : pour écrire les données en format JSON
- random : pour générer les données aléatoires
- string : pour générer des noms de fichiers aléatoires

## Fonctionnalités
Le programme génère les données aléatoires pour chaque entrée en utilisant la fonction `random`. Les valeurs générées pour chaque entrée sont les suivantes :
- "individu" : un entier aléatoire compris entre 0 et 9 inclus
- "x" : un nombre flottant aléatoire compris entre 0 et 5
- "y" : un nombre flottant aléatoire compris entre 0 et 5
- "z" : un nombre flottant aléatoire compris entre 0 et 5
- "temps" : un nombre flottant aléatoire compris entre 0 et 5

Le programme génère également un nom de fichier aléatoire de 5 lettres en utilisant la fonction `choices` de la bibliothèque `string`. Enfin, les données sont écrites dans un fichier JSON avec le nom généré en utilisant la fonction `dump` de la bibliothèque `json`.

## Variables
Le programme utilise la variable suivante :
- NUM_ENTRIES : un entier définissant le nombre d'entrées à générer. Dans le script fourni, cette variable est définie à 10.

## Utilisation
Pour utiliser le programme, exécutez le script Python à partir d'un terminal en vous assurant que vous êtes dans le répertoire contenant le script. Le programme générera alors les fichiers JSON avec les données aléatoires.

## Conclusion
Le programme génère des fichiers JSON avec des données aléatoires pour chaque entrée. Les fichiers générés contiennent les informations d'un individu, y compris les coordonnées x, y et z, ainsi que le temps. Le programme utilise les bibliothèques `json`, `random` et `string` pour générer les données aléatoires et écrire les données en format JSON.```



# UDP_send.py

## Objectif
Ce script Python a pour objectif de surveiller les modifications d'un dossier et d'envoyer les données des fichiers JSON créés dans ce dossier vers un serveur distant via le protocole UDP.

## Fonctionnement
Le script utilise la bibliothèque `watchdog` pour surveiller les modifications du dossier spécifié. Lorsqu'un fichier JSON est créé, son contenu est ajouté à une queue FIFO en mémoire. Les données sont ensuite converties en JSON et envoyées via UDP à un serveur distant. Le fichier JSON est supprimé une fois que les données ont été envoyées avec succès.

## Dépendances
Le script utilise les dépendances suivantes :
- `os` pour supprimer le fichier JSON une fois que les données ont été envoyées avec succès.
- `socket` pour configurer et utiliser la connexion UDP.
- `json` pour convertir les données en JSON.
- `watchdog` pour surveiller les modifications du dossier.
- `collections` pour créer une queue FIFO.

## Configuration
Avant de lancer le script, vous devez configurer les paramètres suivants :
- `UDP_PORT` : définissez le numéro de port UDP à utiliser pour la connexion.
- `sock.sendto` : définissez l'adresse IP et le numéro de port du serveur distant.

## Utilisation
Pour utiliser ce script, lancez-le à partir de la ligne de commande en exécutant la commande `python nom_du_script.py` dans le répertoire contenant le script. Le script surveillera ensuite les modifications du dossier spécifié et enverra les données des fichiers JSON créés à un serveur distant via UDP.

## Limitations
Ce script ne prend pas en charge la mise en file d'attente de plusieurs fichiers JSON en même temps. Il envoie les données du fichier JSON créé dès qu'il est détecté et supprime le fichier immédiatement après l'envoi. De plus, ce script ne prend pas en charge la récupération des données à partir d'un serveur distant, car son objectif principal est d'envoyer les données localement.