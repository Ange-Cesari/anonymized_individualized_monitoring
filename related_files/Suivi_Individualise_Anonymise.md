# Suivi Individualisé Anonymisé

## Définitions:

## Filtre de Kalman

Definition :

**Le filtre de Kalman est une méthode visant à estimer des paramètres d'un système évoluant dans le temps à partir de mesures bruités.**

On retrouve ce filtre dans bon nombre de domaines relatifs au traitement du signal, radar, traitement d'images etc.

*Un exemple d'utilisation de ce filtre pourrait être la détermination de la position et de la vitesse d'un véhicule à partir de données GPS fournis par plusieurs satellites.*

---

## Intelligence artificielle

Definition : 

Modèle de réseau de neurones utilisé pour la détection de personne sur une image a partir de caractéristique de la taille . Le réseau actuellement utilisé est YOLOv3. Cette technique pourra permette à une machine de reproduire des comportements liés aux humains, tel que la planification de déplacement.

---

## Analyse vidéo

Definition : 

Méthode d’étude des données collectées par des caméras

---

## Benchmark

Definition:

Technique de comparaison qui sert à évaluer la performance d’un outil et la comparer aux meilleurs acteurs du secteur

---

## Optimisations

Definition :

Donner à quelque chose les meilleures conditions d'utilisation, de fonctionnement, de rendement, notamment en économie

---

## Prédiction de trajectoire

Definition :

Simulation informatique permettant, à partir de données initiales (position, vitesse, accélération) de prévoir un déplacement en fonction du temps

---

## Analyse comportementale

Definition :

Consiste à observer le comportement d'une personne et utiliser ces données pour évaluer certains aspects de la personne concernée, pouvant être défini comme du profilage

---

## Suivi anonymisé et individualisé :

Definition :

Suivre les individus dans l'espace public et de les identifier de manière anonyme en utilisant des systèmes d’analyse vidéo.

---

## Objectifs:

### Identification des individus sur des vidéos et anonymisation des données.

- Étudier les systèmes d'analyse vidéo existants et identifier les points forts et les points faibles de ces systèmes.
- Déployer un système d'analyse vidéo sur un système dédié à ce domaine (Nvidia Jetson).
- Porter le déploiement sur un système embarqué (Raspberry Pi).
- Validation du système sur des vidéos de "cas réels".
- Extraire les informations nécessaires au suivi anonymisé (positions dans l'image, tailles des individus, **autres**).
    
    Problématiques : 
    
    - Quelles sont les spécifications matérielles minimales permettant d'obtenir une quantité de données suffisante pour l'analyse ?
    - Quelles informations supplémentaires permettant de renforcer la qualité du suivi peuvent être extraites des vidéos tout en conservant l'anonymat des individus ?

### Utilisation des données pour effectuer un suivi individualisé.

- Étudier les systèmes de suivi existants et identifier les points forts et les points faibles de ces systèmes.
- Proposer un système de suivi individualisé basé sur les données extraites des vidéos. Seules ces données pourront être utilisées ensuite.
- Validation du système sur données extraites de vidéos de "cas réels".
    
    Problématiques : 
    
    - Comment renforcer un suivi basé sur des prédictions effectuées à l'aide de méthodes statistique ?
    - Quelles sont les méthodes orientées "Intelligence artificielle" permettant d'obtenir des résultats équivalents (ou supérieurs) à un suivi basé sur des prédictions effectuées à l'aide de méthodes statistiques ?
    - Quelles sont les spécifications matérielles minimales permettant d'obtenir un suivi fonctionnel pour chaque méthode ? Le terme "fonctionnel" représente ici un ensemble de critères factuels (à définir) permettant d'évaluer l'efficacité des méthodes.
    - Une méthode hybride (I.A. et statistique) est-elle possible ?

## Etats de l’art :

- Solutions de tracking commerciales
- Hardware à utiliser (caméras ou GPU)
- Algorithmes (CNN, Kalman)
- Technologies de detections

## Résultats attendus :

- Comment renforcer un suivi basé sur des prédictions effectuées à l'aide de méthodes statistiques ?
- Quelles sont les méthodes orientées "Intelligence artificielle" permettant d'obtenir des résultats équivalents (ou supérieurs) à un suivi basé sur des prédictions effectuées à l'aide de méthodes statistiques ?
- Quelles sont les spécifications matérielles minimales permettant d'obtenir un suivi fonctionnel pour chaque méthode ? Le terme "fonctionnel" représente ici un ensemble de critères factuels (à définir) permettant d'évaluer l'efficacité des méthodes.
- Une méthode hybride (I.A. et statistique) est-elle possible ?

## **Phase de test :**

- **Dataset :**
    
    [https://github.com/jiachenli94/Awesome-Interaction-Aware-Trajectory-Prediction#pedestrians](https://github.com/jiachenli94/Awesome-Interaction-Aware-Trajectory-Prediction#pedestrians)
    
- **Tracking anonymisé : Utilisation de capteur 3D :**
    
    Présentation : [https://dil.atr.jp/crest2010_HRI/ATC_dataset/](https://dil.atr.jp/crest2010_HRI/ATC_dataset/)
    
    Documentation du projet : [https://www.researchgate.net/publication/264580888_Person_Tracking_in_Large_Public_Spaces_Using_3-D_Range_Sensors](https://www.researchgate.net/publication/264580888_Person_Tracking_in_Large_Public_Spaces_Using_3-D_Range_Sensors)
    
    Test capteur 3D + filtre de Kalman pour la prédiction
    
    [https://www.mdpi.com/2072-4292/14/8/1837](https://www.mdpi.com/2072-4292/14/8/1837)
    
- **Prédiction à l’aide des filtres de Kalman :**
    
    [https://github.com/SriramEmarose/Multi-Object-Motion-Prediction-With-KalmanFilter](https://github.com/SriramEmarose/Multi-Object-Motion-Prediction-With-KalmanFilter)
    

Paramètre de forme pour Yolo

## Quels paramètres de formes sont utilisé par YOLO pour différencier 2 personnes ?

YOLO utilise principalement les coordonnées du bounding box, la probabilité de détection et les classes prédites pour différencier entre plusieurs personnes dans une image.

Les coordonnées du bounding box sont les coordonnées du coin supérieur gauche et du coin inférieur droit du rectangle entourant une personne. Elles sont utilisées pour déterminer l'emplacement de chaque personne dans l'image. Si deux bounding boxes se chevauchent, il est probable qu'ils représentent la même personne.

La probabilité de détection et les scores de confiance pour chaque classe prédite peuvent également aider à différencier les personnes, car ils indiquent la certitude de la détection et de la classification de l'objet. Si deux bounding boxes ont des scores de confiance très différents pour la classe "personne", il est probable qu'ils représentent deux personnes différentes.

En utilisant ces paramètres, YOLO peut détecter et différencier plusieurs personnes dans une image.