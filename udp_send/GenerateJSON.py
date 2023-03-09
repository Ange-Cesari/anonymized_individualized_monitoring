import json
import random
import string

# Définir le nombre d'entrées à générer
NUM_ENTRIES = 10

# Générer les données aléatoires pour chaque entrée
for i in range(NUM_ENTRIES):
    data = {
        "individu": random.randint(0, 9),
        "x": random.uniform(0, 5),
        "y": random.uniform(0, 5),
        "z": random.uniform(0, 5),
        "temps": random.uniform(0, 5)
    }
    
    # Générer un nom de fichier aléatoire de 5 lettres
    filename = ''.join(random.choices(string.ascii_lowercase, k=5)) + '.json'
    
    # Écrire les données dans un fichier JSON avec le nom généré
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)