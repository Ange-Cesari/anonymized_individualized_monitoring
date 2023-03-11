Explication détaillée d’un algorithme permettant la détection et reconnaissance d’objets vidéo en mouvement grace au filtre de Kalman et au Deep Learning :

[https://thesai.org/Downloads/Volume12No1/Paper_18-Detection_and_Recognition_of_Moving_Video_Objects.pdf](https://thesai.org/Downloads/Volume12No1/Paper_18-Detection_and_Recognition_of_Moving_Video_Objects.pdf)

**Axe n°1 : Comment réduire les erreurs de détection avec les filtres de kalmann et le deep learning sur des images anonymisées ?**

1. Lisser les données et réduire le bruit dans les images grâce à des filtres de Kalman.
    
    [https://www.rapport-gratuit.com/utilisation-des-filtres-de-kalman-pour-lelimination-de-faux-positifs/](https://www.rapport-gratuit.com/utilisation-des-filtres-de-kalman-pour-lelimination-de-faux-positifs/)
    
    Application d’un filtre gaussien de déviation standard pour réduire le bruit
    

1. Prédire les valeurs manquantes ou incomplètes dans les images grâce au deep learning.
    
    [https://larevueia.fr/4-methodes-pour-gerer-les-donnees-manquantes-en-machine-learning-avec-pandas/](https://larevueia.fr/4-methodes-pour-gerer-les-donnees-manquantes-en-machine-learning-avec-pandas/)
    
    Dans les deux cas nous aurons recours a une architecture de réseau de neurones appropriée, en s'assurant de disposer de suffisamment de couches et de neurones pour capturer les détails complexes de l'image. Nous utiliserons des données d'entraînement (utilisation d'un grand nombre d'images avec des valeurs manquantes ou incomplètes connues) afin d’entraîner le modèle en utilisant une fonction de perte et un algorithme d'optimisation appropriés.
    
    Pour réduire le risques de fuite de données sensibles et pour rentre l’apprentissage le plus efficace possible, les images devront être anonymisé avant leur utilisation pour l'entraînement du modèle de deep learning. 
    
    Le modelé sera testé avec une validation croisée sur les données d'entraînement pour vérifier qu’il est capable de gérer les erreurs.
    

**Axe n°2 : Quel facteur de forme ou de couleur utilisé lors de l’anonymisation des données pour identifier les personnes ?**

1. La silhouette et la taille : les formes du corps et la taille varient d’une personne à l’autre, ainsi on peut utiliser la silhouette et la taille d’une personne pour l’identifier. 
    
    Pour cela on peut utiliser l’algorithme hongrois ( aussi nommé l’algorithme de Kuhn-Munkres) qui peut associer un obstacle d’une image à l’autre, sur la base d’un score. Il permet l’attribution d’id et l’association.
    
    [https://medium.com/france-school-of-ai/tracking-par-computer-vision-90e5111cbb86](https://medium.com/france-school-of-ai/tracking-par-computer-vision-90e5111cbb86)
    
2. Les mouvements du corps : les mouvements du corps tels que la démarche, la gestuelle et la posture : algorithme de détection de mouvement, algorithme de reconnaissance de gestes, algorithme de reconnaissance de démarche.
    
    
3. Les vêtements et les accessoires : les vêtements et les accessoires de pars leurs caractéristiques tels que la forme ou la couleur peuvent être utilisés (chapeau bleu, sac a dos rose, manteau vert…).

**Axe n°3 : Comment prédire les déplacements avec les filtres de kalman ?**

[https://medium.com/france-school-of-ai/la-fusion-de-capteurs-587f91a1423a](https://medium.com/france-school-of-ai/la-fusion-de-capteurs-587f91a1423a)

Doute :

[https://www.youtube.com/watch?v=w7mNyGqpKzM](https://www.youtube.com/watch?v=w7mNyGqpKzM)

[https://www.youtube.com/watch?v=O3b8lVF93jU](https://www.youtube.com/watch?v=O3b8lVF93jU)

[https://www.youtube.com/watch?v=zi-62z-3c4U](https://www.youtube.com/watch?v=zi-62z-3c4U)