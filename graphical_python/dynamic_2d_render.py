"""
CODE WRITTEN BY Ange Cesari
"""
import json
import pygame
import os
import time

# Initialise Pygame
pygame.init()

# Crée une fenêtre Pygame de 800x600 pixels
screen = pygame.display.set_mode((800, 600))

colors = [(0, 0, 255), (255, 0, 255), (255, 255, 255),(0, 255, 255),(0, 255, 0),(100, 0, 0) ]

def humain () : 
    for j in range(6):
        # Boucle pour charger et afficher chaque fichier JSON
        for i in range(20):
            # Construit le nom de fichier pour cette itération
            filename = f'human_{j}_frame_{i}.json'
            
            # Charge le fichier JSON
            with open(filename) as f:
                data = json.load(f)

            # Récupère les coordonnées x, y et le temps t du fichier JSON
            x = data['x']
            y = data['y']
            t = data['t']

            # Vérifie si les coordonnées sont dans la zone de -30 à 30
            if -30 <= x <= 30 and -30 <= y <= 30:
                danger()
                # Convertit les coordonnées en pixels
                px = int((x + 30) * 800 / 60)
                py = int((y + 30) * 600 / 60)
                position = (px, py)

                # Dessine un point bleu à l'emplacement (x, y) sur l'écran
                # screen.fill((0,0,0))
                color = colors[j]
                radius = 5 
                pygame.draw.circle(screen, color, position, radius)
                

                # Affiche le temps t à côté du point
                font = pygame.font.SysFont(None, 24)
                text = font.render(str(t), True, (255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = position
                text_rect.move_ip(10, -10)
                screen.blit(text, text_rect)
                pygame.display.update()
                time.sleep(.1)

               

    # Met à jour l'affichage
    pygame.display.flip()

def danger () :
    # Load JSON file
    with open('danger.json') as f:
        data = json.load(f)

    # Extract x, y coordinates and time t from JSON data
    x = data['x']
    y = data['y']
    t = data['t']

    # Vérifie si les coordonnées sont dans la zone de -30 à 30
    if -30 <= x <= 30 and -30 <= y <= 30:
        # Convertit les coordonnées en pixels
        px = int((x + 30) * 800 / 60)
        py = int((y + 30) * 600 / 60)
        position = (px, py)

        # Dessine un point rouge à l'emplacement (x, y) sur l'écran
        color = (255, 0, 0)
        radius = 5
        pygame.draw.circle(screen, color, position, radius)
        font = pygame.font.SysFont(None, 24)
        text = font.render(str(t), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = position
        text_rect.move_ip(10, -10)
        screen.blit(text, text_rect)

    # Met à jour l'affichage
    pygame.display.flip()

# Appelle les fonctions pour dessiner les points
humain()

if os.path.exists("danger.json"):
    print("Le fichier danger.json existe dans le répertoire courant.")
    danger()
else:
    print("Le fichier danger.json n'existe pas dans le répertoire courant.")


# Boucle de jeu principale
while True:
    # Gère les événements Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quitte le programme si l'utilisateur ferme la fenêtre
            pygame.quit()
            quit()