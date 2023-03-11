# Trajectoires Pygame : Simulation de déplacement aléatoire de foule

Ce script simule le déplacement aléatoire de personnes dans un espace fermé. Les personnes sont représentées par des cercles de rayon `PERSON_RADIUS` et de couleur `PERSON_COLOR`. La simulation prend en compte la répulsion des personnes les unes par rapport aux autres ainsi que la direction globale dans laquelle elles se déplacent.

## Paramètres

* `WINDOW_WIDTH` : Largeur de la fenêtre en pixels.
* `WINDOW_HEIGHT` : Hauteur de la fenêtre en pixels.
* `BG_COLOR` : Couleur de fond de la fenêtre.
* `NUM_PEOPLE` : Nombre de personnes dans la simulation.
* `PERSON_RADIUS` : Rayon des cercles représentant les personnes.
* `PERSON_COLOR` : Couleur des cercles représentant les personnes.
* `MAX_SPEED` : Vitesse maximale des personnes en pixels par itération.
* `MAX_ACCEL` : Accélération maximale des personnes en pixels par itération au carré.
* `WALL_PADDING` : Distance minimale des personnes par rapport aux bords de la fenêtre.

## Classe `Person`

### Attributs

* `x` : Coordonnée x de la position de la personne.
* `y` : Coordonnée y de la position de la personne.
* `vx` : Composante x de la vitesse de la personne.
* `vy` : Composante y de la vitesse de la personne.

### Méthodes

* `update(self, goal_x, goal_y, people)` : Met à jour la position et la vitesse de la personne. Prend en compte les interactions avec les autres personnes ainsi que la direction globale de déplacement.


# 2d_simulation_generation.py


## Constantes

- `NUM_HUMANS`: le nombre de personnes dans la simulation.
- `SIMULATION_TIME`: le temps total de la simulation en secondes.
- `FRAME_INTERVAL`: l'intervalle de temps entre chaque image (frame) de la simulation en secondes.
- `MIN_X_RANGE`: la plage minimale de l'axe X où les personnes peuvent apparaître.
- `MAX_X_RANGE`: la plage maximale de l'axe X où les personnes peuvent apparaître.
- `MIN_Y_RANGE`: la plage minimale de l'axe Y où les personnes peuvent apparaître.
- `MAX_Y_RANGE`: la plage maximale de l'axe Y où les personnes peuvent apparaître.
- `DANGER_RANGE`: la plage où le danger peut apparaître.
- `DANGER_RADIUS`: le rayon du danger.

## Classe `Human`

Cette classe représente une personne dans la simulation. Elle possède les attributs suivants :

- `id`: un identifiant unique pour chaque personne.
- `x`: la position de la personne sur l'axe X.
- `y`: la position de la personne sur l'axe Y.
- `vx`: la vitesse horizontale de la personne.
- `vy`: la vitesse verticale de la personne.

La classe `Human` possède également les méthodes suivantes :

- `__init__(self, human_id)`: le constructeur de la classe `Human`. Il prend un argument `human_id` qui est l'identifiant unique de la personne.
- `update_position(self, dt)`: met à jour la position de la personne en fonction de sa vitesse et de l'intervalle de temps `dt`.
- `generate_speed(self)`: génère une vitesse aléatoire pour la personne.
- `update_speed(self, danger_x, danger_y)`: met à jour la vitesse de la personne en fonction de sa distance par rapport au danger.

La méthode `to_dict(self, t)` est utilisée pour convertir l'objet `Human` en un dictionnaire JSON avec les propriétés suivantes :

- `"x"`: la position de la personne sur l'axe X.
- `"y"`: la position de la personne sur l'axe Y.
- `"t"`: le temps écoulé depuis le début de la simulation.
- `"s_x"`: la vitesse horizontale de la personne.
- `"s_y"`: la vitesse verticale de la personne.

## Classe `Danger`

Cette classe représente un danger dans la simulation. Elle possède les attributs suivants :

- `x`: la position du danger sur l'axe X.
- `y`: la position du danger sur l'axe Y.
- `t`: le temps où le danger est apparu.

La méthode `to_dict(self)` est utilisée pour convertir l'objet `Danger` en un dictionnaire JSON avec les propriétés suivantes :

- `"x"`: la position du danger sur l'axe X.
- `"y"`: la position du danger sur l'axe Y.
- `"t"`: le temps où le danger est apparu.

## Fonctions de déplacement

La méthode `update_position` de la classe `Human` met à jour la position de la personne en fonction de sa vitesse et de l'intervalle de temps `dt`. La méthode `generate_speed` génère une vitesse aléatoire pour la personne. La méthode `update_speed` met à jour la vitesse de la personne en fonction de sa distance par rapport au danger


## Utilisation de JSON
Le module `json` est utilisé pour sérialiser et désérialiser des données JSON. Dans ce script, il est utilisé pour sauvegarder les données de chaque personne et de chaque danger dans un fichier JSON.

La méthode `to_dict` est appelée sur chaque instance de la classe Human et Danger pour retourner un dictionnaire contenant les propriétés de l'instance, qui est ensuite sérialisé dans un fichier JSON à l'aide de la méthode json.dump.

La méthode `json.load` peut être utilisée pour charger les données d'un fichier JSON et les désérialiser en un objet Python. Cela pourrait être utile si vous vouliez charger les données d'une simulation précédente et continuer à la simuler à partir de là.


