import os
import socket
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from collections import deque

# Définir le numéro de port UDP
UDP_PORT = 38945

# Configurer la connexion UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Créer une queue FIFO
queue = deque()

# Créer un gestionnaire d'événements de système de fichiers pour surveiller les modifications du dossier
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Si un fichier JSON est créé, ouvrir le fichier et ajouter son contenu à la queue
        if event.is_directory:
            return None
        elif event.event_type == 'created' and event.src_path.endswith('.json'):
            with open(event.src_path, 'r') as f:
                data = json.load(f)
                queue.append(data)
            # Convertir les données en JSON et les envoyer via UDP
            message = json.dumps(data).encode('utf-8')
            sock.sendto(message, ('localhost', UDP_PORT))
            # Imprimer les données envoyées dans la console
            print("Données envoyées : ", data)
            # Supprimer le fichier JSON
            os.remove(event.src_path)

# Surveiller les modifications du dossier
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, '.', recursive=False)
observer.start()

# Boucle principale pour envoyer les données en continu
try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()