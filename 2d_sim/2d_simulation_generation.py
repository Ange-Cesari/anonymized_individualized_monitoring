"""
CODE WRITTEN BY Ange Cesari
"""
import random
import json
import os

if os.path.exists("danger.json"):
    os.remove("danger.json")

# Définition des constantes
NUM_HUMANS = 10
SIMULATION_TIME = 10
FRAME_INTERVAL = 0.5

MIN_X_RANGE = (-35, -30)
MAX_X_RANGE = (30, 35)
MIN_Y_RANGE = (-35, -30)
MAX_Y_RANGE = (30, 35)
DANGER_RANGE = (-20, 20)
DANGER_RADIUS = 10



# Définition de la classe Human
class Human:
    MAX_SPEED_NEG = -4
    MIN_SPEED_NEG = -2
    MIN_SPEED_POS = 2
    MAX_SPEED_POS = 4

    
    def __init__(self, human_id):
        self.id = human_id
        self.x = random.uniform(*MIN_X_RANGE) if human_id < NUM_HUMANS // 2 else random.uniform(*MAX_X_RANGE)
        self.y = random.uniform(*MIN_Y_RANGE) if human_id < NUM_HUMANS // 2 else random.uniform(*MAX_Y_RANGE)

        self.vx = self.generate_speed()
        self.vy = self.generate_speed()


    def update_position(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def generate_speed(self):
        return random.choice(
            [
                random.uniform(self.MIN_SPEED_NEG, self.MAX_SPEED_NEG),
                random.uniform(self.MIN_SPEED_POS, self.MAX_SPEED_POS),
            ]
        )

    def update_speed(self, danger_x, danger_y):
        # Calculer la distance entre la personne et le danger
        distance = ((self.x - danger_x) ** 2 + (self.y - danger_y) ** 2) ** 0.5
        
        # Obtenir la direction actuelle de la personne
        dx, dy = self.vx, self.vy
        
        # Si la personne est à une distance inférieure au rayon de danger, mettre à jour la vitesse
        if distance < DANGER_RADIUS:
            # Obtenir la direction du danger par rapport à la personne
            dir_x, dir_y = danger_x - self.x, danger_y - self.y
            
            # Normaliser le vecteur direction pour obtenir une direction unitaire
            dir_norm = (dir_x ** 2 + dir_y ** 2) ** 0.5
            dir_x, dir_y = dir_x / dir_norm, dir_y / dir_norm
            
            # Obtenir le produit scalaire entre la direction actuelle de la personne et la direction du danger
            prod_scal = dx * dir_x + dy * dir_y
            
            # Si la personne se déplace vers le danger, inverser la direction de la personne
            if prod_scal > 0:
                # Inverser la direction la plus proche du danger
                if abs(dir_x) > abs(dir_y):
                    self.vx = -dx * 2
                else:
                    self.vy = -dy * 2

    def to_dict(self, t):
        return {"x": self.x, "y": self.y, "t": t, "s_x": self.vx, "s_y": self.vy}

# Définition de la classe Danger
class Danger:
    def __init__(self, t):
        self.x = random.uniform(*DANGER_RANGE)
        self.y = random.uniform(*DANGER_RANGE)
        self.t = t

    def to_dict(self):
        return {"x": self.x, "y": self.y, "t": self.t}

# Initialisation des humains
humans = [Human(i) for i in range(NUM_HUMANS)]

# Initialisation de la variable danger à None
danger = None

# Boucle principale de la simulation
for i in range(int(SIMULATION_TIME / FRAME_INTERVAL)):
    t = i * FRAME_INTERVAL
    # Génération aléatoire de la probabilité qu'un danger apparaisse
    if danger is None and random.random() < 0.2:
        danger_time = t  # Le temps du danger est maintenant égal à t
        danger = Danger(danger_time)
    for human in humans:
        human.update_position(FRAME_INTERVAL)
        if danger is not None:
            human.update_speed(danger.x, danger.y)
        filename = f"human_{human.id}_frame_{i}.json"
        with open(filename, "w") as f:
            json.dump(human.to_dict(t), f)
    if danger is not None:
        with open("danger.json", "w") as f:
            json.dump(danger.to_dict(), f)
    #danger = None if danger is not None and t >= danger.t else danger  # Mettre danger à None si le danger a eu lieu