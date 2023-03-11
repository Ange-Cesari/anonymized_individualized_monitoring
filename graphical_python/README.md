Readme for the graphical_python folder that includes the necessary scripts using tkinter or pygame and explanations

# 3d_perspective_render

Ce programme utilise la bibliothèque Tkinter pour afficher une simulation de points en 3D.

## Paramètres

- `WIDTH` : La largeur de la fenêtre de simulation.
- `HEIGHT` : La hauteur de la fenêtre de simulation.
- `X_RANGE` : La plage de valeurs pour les coordonnées x des points.
- `Y_RANGE` : La plage de valeurs pour les coordonnées y des points.
- `Z_RANGE` : La plage de valeurs pour les coordonnées z des points.
- `N_POINTS` : Le nombre de points à afficher.
- `colors` : Les couleurs possibles pour les points.
- `camera_x` : La position x de la caméra.
- `camera_y` : La position y de la caméra.
- `camera_z` : La position z de la caméra.
- `zoom_factor` : Le facteur de zoom.

## Fonctions

- `project(point)` : Convertit les coordonnées 3D d'un point en coordonnées 2D.
- `draw_points()` : Dessine les points sur le canevas.

## Déroulement du programme

- Génération des points avec des coordonnées aléatoires dans les plages spécifiées.
- Création de la fenêtre de simulation.
- Création du canevas pour dessiner les points.
- Dessin des points en appelant la fonction `draw_points()`.
- Boucle principale d'affichage de la fenêtre de simulation.


# dynamic_2d_render.py

## Introduction

Le code fourni est un programme Python qui utilise la bibliothèque Pygame pour dessiner des points sur un écran en fonction de données stockées dans des fichiers JSON. Le programme lit des fichiers JSON contenant des coordonnées x, y et un temps t et dessine des points sur l'écran en utilisant les coordonnées lues. Il y a deux types de fichiers JSON : `human_{j}_frame_{i}.json` et `danger.json`.

Le programme dessine des points bleus pour les coordonnées x, y stockées dans les fichiers JSON `human_{j}_frame_{i}.json`. Pour les coordonnées stockées dans le fichier JSON `danger.json`, il dessine des points rouges. Les points sont dessinés à l'emplacement correspondant aux coordonnées x, y converties en pixels, avec l'heure t affichée à côté du point.

 ## Bibliothèques

 Le programme utilise les bibliothèques suivantes :

 - `json` :  pour lire les fichiers JSON contenant les coordonnées et le temps
 - `pygame` : pour dessiner les points sur l'écran
 - `os` : pour vérifier si un fichier existe

 ## Fonctions 
 Le programme utilise deux fonctions :
 - `humain() `: Cette fonction lit les fichiers JSON `human_{j}_frame_{i}.json` et dessine des points bleus sur l'écran en utilisant les coordonnées x, y stockées dans le fichier. Elle affiche également l'heure t à côté du point et vérifie si les coordonnées sont dans la zone de -30 à 30. Cette fonction utilise la fonction `danger()` pour dessiner des points rouges si les coordonnées stockées dans `danger.json` sont dans la zone de -30 à 30.
 - `danger()`: Cette fonction lit le fichier JSON `danger.json` et dessine des points rouges sur l'écran en utilisant les coordonnées x, y stockées dans le fichier. Elle affiche également l'heure t à côté du point et vérifie si les coordonnées sont dans la zone de -30 à 30.

 ## Boucle principale

 Le programme utilise une boucle principale `while True` pour gérer les événements Pygame. Si l'utilisateur ferme la fenêtre, la boucle principale se termine et le programme se ferme.


## Conclusion

En somme, le programme lit les coordonnées x, y et le temps t stockés dans les fichiers JSON et dessine des points sur l'écran en utilisant ces coordonnées. Les points bleus sont dessinés pour les coordonnées stockées dans `human_{j}_frame_{i}.json` et les points rouges pour les coordonnées stockées dans `danger.json`. Les coordonnées sont converties en pixels et affichées à l'écran, avec l'heure t. Le programme utilise la bibliothèque Pygame pour dessiner les points et la boucle principale pour gérer les événements Pygame.

## Améliorations possibles : 
Les améliorations : 

Différents types de dangers : Une bouche d'egout n'est pas le même type de danger qu'un feu qui se propage, ou que d'attaque.
Le comportement des humains devrait être différent en fonction des niveaux de risques. Une bouche d'égout devrait être "contournable" mais conserver la trajectoire d'origine, tandis qu'un feu qui se propage ou une attaque devrait mener à une fuite des humains vers l'endroit opposé au danger.



Lorsqu'un humain voit un autre humain courir, il devrait également se mettre à courir. 
nécessite d'avoir la compréhension de son environnement et la détection des autres joueurs. 
Nécessitent d'avoir un "état" relatif à chaque humain pour savoir s'ils sont en train de marcher ou en fuite.

