"""
CODE WRITTEN BY Ange Cesari
"""
import random
import json

Humans = []
HUMAN_NUM = 4
SIMULATION_TIME = 10
FRAME_INTERVAL = 0.5
TOTAL_FRAMES = int(SIMULATION_TIME / FRAME_INTERVAL) # nombre total de frames de la simulation

def generate_human():
    """
    Fonction qui génère un individu avec des coordonnées et une vitesse aléatoire.
    Les coordonnées x et y sont comprises entre -30 et 30, et la coordonnée z entre -10 et 10.
    La vitesse est générée aléatoirement entre -5 et 5 pour les coordonnées x et y,
    et entre -2 et 2 pour la coordonnée z.
    """
    return {
        'id': len(Humans),
        'x': random.uniform(-30, 30),
        'y': random.uniform(-30, 30),
        'z': random.uniform(-10, 10),
        's_x': random.uniform(-5, 5),
        's_y': random.uniform(-5, 5),
        's_z': random.uniform(-2, 2)
    }

def update_human(human):
    """
    Fonction qui met à jour la position de l'individu en fonction de sa vitesse.
    """
    human['x'] += human['s_x'] * FRAME_INTERVAL
    human['y'] += human['s_y'] * FRAME_INTERVAL
    human['z'] += human['s_z'] * FRAME_INTERVAL
    
    # Mise à jour du temps de la simulation
    human['t'] = CURRENT_FRAME

def run_simulation():
    """
    Fonction qui lance la simulation pour une durée de 10 secondes avec une fréquence de 0.5 seconde.
    """
    global CURRENT_FRAME, Humans
    for i in range(TOTAL_FRAMES):
        CURRENT_FRAME = i * FRAME_INTERVAL
        # Génération des individus manquants
        while len(Humans) < HUMAN_NUM:
            Humans.append(generate_human())
        # Mise à jour de la position des individus
        for human in Humans:
            update_human(human)
        # Enregistrement des coordonnées de chaque individu
        for human in Humans:
            json.dump(
                {'x': human['x'], 'y': human['y'], 'z': human['z'], 't': CURRENT_FRAME, 's_x': human['s_x'], 's_y': human['s_y'], 's_z': human['s_z']},
                open(f'human_{human["id"]}_frame_{i}.json', 'w')
            )

run_simulation()