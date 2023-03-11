"""
CODE WRITTEN BY Aurélie Martin
"""
import pygame
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
import math

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = (255, 255, 255)

# Paramètres de la simulation
NUM_PEOPLE = 20
PERSON_RADIUS = 10
PERSON_COLOR = (0, 0, 255)
MAX_SPEED = 3
MAX_ACCEL = 0.2
WALL_PADDING = 100

array_color: list = []

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Simulation de déplacement aléatoire de foule")
my_font = pygame.font.SysFont('Comic Sans MS', 10)


# Classe pour représenter une personne
class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def update(self, goal_x, goal_y, people):
        # Calcul d'une direction aléatoire
        random_direction = (random.uniform(-1, 1), random.uniform(-1, 1))

        # Calcul de la force de répulsion des autres personnes
        repulsion_x = 0
        repulsion_y = 0
        for other in people:
            if other == self:
                continue
            dx = other.x - self.x
            dy = other.y - self.y
            distance_to_other = ((dx ** 2) + (dy ** 2)) ** 0.5
            if distance_to_other < 5 * PERSON_RADIUS:
                repulsion_x -= dx / (distance_to_other ** 2)
                repulsion_y -= dy / (distance_to_other ** 2)

        # Mise à jour de la vitesse et de la position
        accel_x = random_direction[0] + repulsion_x
        accel_y = random_direction[1] + repulsion_y
        
        # Appliquer la direction plus directe
        dx_goal = goal_x - self.x if goal_x is not None else 0
        dy_goal = goal_y - self.y if goal_y is not None else 0
        accel_x += dx_goal / 100
        accel_y += dy_goal / 100
        
        accel = ((accel_x ** 2) + (accel_y ** 2)) ** 0.5
        if accel > MAX_ACCEL:
            accel_x *= MAX_ACCEL / accel
            accel_y *= MAX_ACCEL / accel
        self.vx += accel_x
        self.vy += accel_y
        speed = ((self.vx ** 2) + (self.vy ** 2)) ** 0.5
        if speed > MAX_SPEED:
            self.vx *= MAX_SPEED / speed
            self.vy *= MAX_SPEED / speed

        if self.x >= WINDOW_WIDTH or self.y >= WINDOW_HEIGHT:
            self.x = 30
            self.y = 30

        if self.x >= (WINDOW_WIDTH-30) and self.y >= (WINDOW_HEIGHT-30):
            self.x = 40
            self.y = WINDOW_HEIGHT/2

        if  self.x <= 30 and self.y <= 30:
            self.x = 40
            self.y = WINDOW_HEIGHT/2
        
        if self.x <= 0 or self.y <= 0:
            self.x = WINDOW_WIDTH - 30
            self.y = WINDOW_HEIGHT - 30
        
        self.x += self.vx
        self.y += self.vy

    def draw(self, person_color,person_number):
        if person_number == 0:
            pygame.draw.circle(window, person_color, (int(self.x), int(self.y)), PERSON_RADIUS*1.5)
            text_surface = my_font.render(f"X : {self.x}, Y : {self.y}", False, (0, 0, 0))
            window.blit(text_surface, (0,0))
        else :
            pygame.draw.circle(window, person_color, (int(self.x), int(self.y)), PERSON_RADIUS)


# Création des personnes
people = []
for i in range(NUM_PEOPLE):
    x = random.randint(WALL_PADDING, WINDOW_WIDTH - WALL_PADDING)
    y = random.randint(WALL_PADDING, WINDOW_HEIGHT - WALL_PADDING)
    person = Person(x, y)
    people.append(person)

# Boucle principale
clock = pygame.time.Clock()
running = True

for i in range(0,NUM_PEOPLE):
    if i not in array_color:
        array_color.append((random.randint(0,220),random.randint(0,140),random.randint(0,180)))
while running:
    counter = 0
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour de la simulation
    for person in people:
        person.update(None, None, people)

    # Affichage des éléments
    window.fill(BG_COLOR)
    for person,color in zip(people,array_color):
        person.draw(color,counter)
        counter+=1
    pygame.display.flip()

    # Limitation de la vitesse de la simulation
    clock.tick(60)

# Fermeture de Pygame
pygame.quit()
plt.close()
