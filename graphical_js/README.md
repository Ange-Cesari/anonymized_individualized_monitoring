Le partie de rendu graphique de JS se base sur des données reçues en UDP. Ces données sur récupérées par le script "broker.js" 
La partie simulation 3d utilise Threejs et est visible via sim.html qui contient le script threejs.


# broker.js



Le code écoute les données UDP envoyées sur un port spécifié, stocke les positions des individus dans un tableau, leur attribue une couleur aléatoire et écrit les données dans des fichiers JSON toutes les 0,5 secondes.

## Fonctionnalités

Le code  permet de :

- Écouter les données UDP envoyées sur un port spécifié.
- Stocker les positions des individus dans un tableau.
- Attribuer une couleur aléatoire à chaque identifiant d'individu.
- Écrire les données dans des fichiers JSON toutes les 0,5 secondes.

## Variables

- `PORT` : Le numéro de port UDP à écouter.
- `positions` : Un tableau des positions des individus.
- `colors` : Un tableau des couleurs associées aux individus.
- `MAX_INDIVIDUS` : Le nombre maximum d'individus.
- `time` : Le temps actuel.

## Fonctions

- `addPosition(id, x, y, z, t)` : Ajoute une position dans le tableau des positions pour un identifiant d'individu donné.
- `prepareDataForJSON()` : Prépare les données pour l'écriture dans un fichier JSON.

## Listener

- `server` : Le serveur UDP qui écoute les données.

## Méthodes du serveur

- `on('error', callback)` : Appelée si une erreur survient lors de l'écoute.
- `on('message', callback)` : Appelée lorsqu'un message est reçu.
- `on('listening', callback)` : Appelée lorsque le serveur commence à écouter.

## Boucle d'écriture

- `setInterval(callback, 500)` : Écrit les données dans des fichiers JSON toutes les 0,5 secondes.

## Divers

- `Math.random()` : Génère un nombre aléatoire entre 0 et 1.
- `Math.floor()` : Arrondit un nombre à l'entier inférieur le plus proche.
- `toString()` : Convertit un objet en chaîne de caractères.
- `JSON.parse()` : Analyse une chaîne de caractères JSON et renvoie un objet JavaScript.
- `JSON.stringify()` : Convertit un objet JavaScript en chaîne de caractères JSON.
- `fs.writeFile()` : Écrit des données dans un fichier.

## Run le script : 

```
node broker.js
```

# Sim.html 

Ce code utilise la bibliothèque Three.js pour créer une scène 3D affichant des points colorés à partir d'un fichier JSON. Voici un aperçu de la logique principale :

- Création d'une scène 3D avec un fond noir
- Création d'une caméra avec une perspective 3D
- Création d'un render pour afficher la scène
- Création de points pour l'affichage
- Création d'un axe x, y et z avec des lignes grises
- Lecture d'un fichier JSON avec une fonction lecture()
- Pour chaque objet dans le fichier JSON, création d'un point 3D et d'une couleur correspondante
- Ajout de ces points à la scène
- Création d'une animation pour afficher la scène en boucle