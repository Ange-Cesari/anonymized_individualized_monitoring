# Documentation du script Python

## Introduction

Le script fourni est un programme Python qui écoute les données en continu via une connexion UDP sur un port spécifié. Il utilise la bibliothèque `socket` pour configurer la connexion et la bibliothèque `json` pour décoder les messages reçus. Les données reçues sont stockées dans une queue `deque`.

## Bibliothèques

Le script utilise les bibliothèques suivantes :

- `socket` : pour configurer la connexion UDP
- `json` : pour décoder les messages reçus
- `collections` : pour créer une queue `deque`

## Variables

Le script utilise la variable suivante :

- `UDP_PORT` : le numéro de port UDP sur lequel le script écoute les données

## Configuration

Le numéro de port UDP est défini par la constante `UDP_PORT`, qui est initialisée à 38945. La connexion UDP est configurée en créant une socket et en la liant à l'adresse locale localhost et au numéro de port défini.

Une queue FIFO est créée en utilisant `collections.deque()`. Les données seront ajoutées à cette queue et enregistrées dans l'ordre de leur réception.

## Fonctions

Le script ne contient aucune fonction.

## Boucle principale

Le script utilise une boucle principale `while True` pour écouter en continu les données via la connexion UDP. Les données reçues sont stockées dans la queue `deque` avec la méthode `append`. Le script imprime les nouvelles données reçues ainsi que toutes les données enregistrées dans la queue à chaque nouvelle donnée reçue.

## utilisation 

Pour utiliser ce script, il suffit de l'exécuter dans un terminal ou une console Python. Les données envoyées via UDP doivent être des messages JSON valides.

Lorsque de nouvelles données sont reçues, elles seront imprimées dans la console, suivies de toutes les données enregistrées dans la queue. Les données restent enregistrées dans la queue jusqu'à ce que le script soit arrêté.

## Conclusion

En somme, le script écoute en continu les données via une connexion UDP sur un port spécifié. Les données reçues sont stockées dans une queue `deque`. Le script utilise la bibliothèque `socket` pour configurer la connexion, la bibliothèque `json` pour décoder les messages reçus et la boucle principale pour écouter les données en continu.```