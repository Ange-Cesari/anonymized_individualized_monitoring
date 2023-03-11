# Prédicteur de trajectoire basé sur l'algorithme de Kalman et les propriétés de Markov

Ce code implémente un prédicteur de trajectoire utilisant un filtre de Kalman discret pour la prédiction. L'algorithme utilise certaines propriétés de Markov (observation et état) pour améliorer la prédiction.

## Classe KalmanMarkovPredictor

La classe `KalmanMarkovPredictor` contient les méthodes suivantes :

### `__init__`

Le constructeur de la classe qui initialise toutes les variables utiles pour le filtre de Kalman et le modèle de Markov.

### `predict`

Une méthode qui prédit la prochaine position de la trajectoire en utilisant la matrice de transition et la matrice de bruit de processus.

### `update`

Une méthode qui met à jour la position de la trajectoire en utilisant la matrice d'observation, la matrice de bruit d'observation et la prédiction précédente.

### `generate_trajectory`

Une méthode qui génère une trajectoire en utilisant la prédiction et la mise à jour.

## Génération de trajectoire

La génération de trajectoire se fait à travers les étapes suivantes :

1. Définition des paramètres pour le filtre de Kalman et le modèle de Markov.
2. Génération d'une trajectoire prédite en utilisant la classe `KalmanMarkovPredictor`.
3. Génération de la vraie trajectoire en utilisant la matrice d'observation et la trajectoire prédite.
4. Affichage des résultats en utilisant Matplotlib.

## Affichage des résultats

Le script utilise Matplotlib pour l'affichage des résultats. Plus précisément, il affiche deux sous-graphes et une animation. Le premier sous-graphique affiche la vraie trajectoire de la cible tandis que le deuxième affiche la trajectoire prédite. L'animation montre l'évolution de la trajectoire prédite à travers le temps.

## Structure du script

Le script peut être divisé en trois parties principales :

1. La définition des paramètres pour le filtre de Kalman et le modèle de Markov.
2. La génération et la prédiction de la trajectoire.
3. L'affichage des résultats.


## Algorithme de Kalman
L'algorithme de Kalman est un filtre utilisé pour estimer l'état d'un système dynamique à partir d'une série d'observations bruitées. Il est basé sur une approche probabiliste et utilise des estimations successives de l'état pour améliorer la prédiction de l'état futur.

L'algorithme de Kalman utilise deux types d'équations : les équations de prédiction et les équations de mise à jour. Les équations de prédiction sont utilisées pour prédire l'état futur du système en utilisant l'état actuel et la commande de contrôle, s'il y en a une. Les équations de mise à jour sont utilisées pour mettre à jour l'estimation de l'état à partir des observations.

La prédiction et la mise à jour de l'état sont effectuées en utilisant des matrices de transition et des matrices d'observation. La matrice de transition est utilisée pour prédire l'état futur, tandis que la matrice d'observation est utilisée pour mettre à jour l'estimation de l'état à partir des observations.

L'algorithme de Kalman est largement utilisé dans les applications de suivi d'objets, de navigation, de contrôle et de reconnaissance de formes.

## Filtre de Kalman discret
Le filtre de Kalman discret est une version discrète de l'algorithme de Kalman utilisé pour les systèmes à temps discret. Il est basé sur les mêmes principes que l'algorithme de Kalman, mais utilise des équations discrètes pour la prédiction et la mise à jour de l'état.

Le filtre de Kalman discret utilise les mêmes matrices de transition et d'observation que l'algorithme de Kalman. Cependant, il utilise également une matrice de bruit de processus et une matrice de bruit d'observation pour tenir compte des incertitudes dans le système et dans les observations.

Prédicteur de trajectoire Kalman-Markov
Le prédicteur de trajectoire Kalman-Markov est un algorithme de prédiction de trajectoire utilisant l'algorithme de Kalman et certaines propriétés de Markov. Il utilise un filtre de Kalman discret pour la prédiction de la trajectoire et une approche probabiliste pour améliorer la prédiction.

Le prédicteur de trajectoire Kalman-Markov utilise les matrices de transition et d'observation du filtre de Kalman discret pour la prédiction et la mise à jour de l'état. Il utilise également une matrice de bruit de processus et une matrice de bruit d'observation pour tenir compte des incertitudes dans le système et dans les observations.

Le prédicteur de trajectoire Kalman-Markov est largement utilisé dans les applications de suivi d'objets, de navigation et de reconnaissance de formes. Il est particulièrement utile pour les objets qui ont des trajectoires imprévisibles ou qui sont soumis à des perturbations.