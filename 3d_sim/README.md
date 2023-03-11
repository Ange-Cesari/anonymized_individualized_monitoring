# Documentation du script de simulation

## Introduction

Ce script permet de simuler le déplacement de plusieurs individus dans un espace tridimensionnel. Les coordonnées de chaque individu sont enregistrées dans un fichier au format JSON à chaque intervalle de temps défini. Le script génère également automatiquement les individus manquants pour atteindre un nombre donné.

## Variables

- `Humans` : liste des individus générés
- `HUMAN_NUM` : nombre d'individus désiré
- `SIMULATION_TIME` : durée de la simulation en secondes
- `FRAME_INTERVAL` : intervalle de temps entre chaque enregistrement de coordonnées
- `TOTAL_FRAMES` : nombre total de frames de la simulation

## Fonctions

- `generate_human()` : génère un individu avec des coordonnées et une vitesse aléatoire.
- `update_human(human)` : met à jour la position de l'individu en fonction de sa vitesse.
- `run_simulation()` : lance la simulation pour une durée de 10 secondes avec une fréquence de 0.5 seconde.

## Enregistrement des coordonnées

Les coordonnées de chaque individu sont enregistrées dans un fichier JSON à chaque intervalle de temps défini. Le fichier est nommé selon le format suivant : `human_[id]_frame_[frame_number].json`. Les données enregistrées sont les coordonnées x, y et z, la vitesse sur chaque axe, et le temps écoulé depuis le début de la simulation.

## Coordonnées : 

Les coordonnées x, y et z représentent respectivement la position de l'individu sur les axes x, y et z dans un espace en trois dimensions. Elles sont initialisées aléatoirement dans la fonction `generate_human()` avec des valeurs comprises entre -30 et 30 pour les coordonnées x et y, et entre -10 et 10 pour la coordonnée z.

Ces coordonnées sont utilisées dans la fonction `update_human(human)` pour mettre à jour la position de chaque individu à chaque frame de la simulation. La fonction `update_human(human)` utilise les vitesses `s_x`, `s_y` et `s_z` de chaque individu pour mettre à jour sa position. Les nouvelles coordonnées sont calculées en multipliant chaque vitesse par l'intervalle de temps entre deux frames (FRAME_INTERVAL) et en ajoutant le résultat à la position actuelle de l'individu.

Les coordonnées x, y et z sont également enregistrées dans un fichier JSON pour chaque frame de la simulation à l'aide de la fonction json.dump(). Les fichiers JSON contiennent les coordonnées x, y et z, ainsi que l'instant t correspondant à la frame et les vitesses `s_x`, `s_y` et `s_z` de chaque individu.