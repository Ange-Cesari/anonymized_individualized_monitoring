import socket
import json
from collections import deque

# Définir le numéro de port UDP
UDP_PORT = 38945

# Configurer la connexion UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', UDP_PORT))

# Créer une queue FIFO
queue = deque()

# Écouter les données en continu
print("Début de l'enregistrement")
while True:
    # Recevoir les données via UDP
    message, address = sock.recvfrom(1024)
    data = json.loads(message.decode('utf-8'))
    # Ajouter les données à une queue
    queue.append(data)
    # Imprimer la nouvelle donnée dans la console
    print("Nouvelle information reçue : ", data)
    # Imprimer toutes les données dans la console en parcourant la queue
    print("Données enregistrées : ")
    for d in queue:
        print(d)