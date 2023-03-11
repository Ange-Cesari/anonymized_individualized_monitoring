"""
CODE WRITTEN BY Ange Cesari
"""
import tkinter as tk
import random

WIDTH = 800
HEIGHT = 800

# Plage de valeurs pour les coordonnées x, y et z
X_RANGE = (-30, 30)
Y_RANGE = (-30, 30)
Z_RANGE = (-10, 10)

# Nombre de points à afficher
N_POINTS = 10

# Couleurs possibles pour les points
colors = ['#FF5733', '#F44336', '#9C27B0', '#3F51B5', '#4CAF50', '#CDDC39', '#FFEB3B', '#FF9800']

# Position de la caméra
camera_x = 0
camera_y = 0
camera_z = 15

# Facteur de zoom
zoom_factor = 10

# Liste des points à afficher
points = [(random.uniform(*X_RANGE), random.uniform(*Y_RANGE), random.uniform(*Z_RANGE)) for _ in range(N_POINTS)]

# Fonction de conversion de coordonnées 3D à 2D
def project(point):
    x, y, z = point
    x = WIDTH/2 + (x - camera_x) * zoom_factor
    y = HEIGHT/2 - (y - camera_y) * zoom_factor
    z = (camera_z - z) * zoom_factor
    return (x, y, z)

# Fonction pour dessiner les points
def draw_points():
    for i, point in enumerate(points):
        x, y, z = project(point)
        color = colors[i % len(colors)]
        canvas.create_oval(x-4-z/4, y-4-z/4, x+4+z/4, y+4+z/4, fill=color, outline=color)

# Création de la fenêtre
root = tk.Tk()
root.title("Simulation")

# Création du canevas pour dessiner les points
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#222222")
canvas.pack()

# Dessin des points
draw_points()

# Boucle principale d'affichage
root.mainloop()