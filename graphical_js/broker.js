//CODE WRITTEN BY Ange Cesari

const PORT = 1234; // numéro de port UDP à écouter
const dgram = require('dgram');
const server = dgram.createSocket('udp4');
const fs = require('fs');

const positions = {}; // tableau des positions des individus
const colors = {}; // tableau des couleurs associées aux individus
const MAX_INDIVIDUS = 10; // nombre maximum d'individus
let time = 0.0; // temps actuel

// fonction pour ajouter une position dans le tableau
function addPosition(id, x, y, z, t) {
  if (!(id in positions)) {
    positions[id] = [];
  }
  positions[id].push({ x, y, z, t });
}

// fonction pour préparer les données pour l'écriture dans un fichier JSON
function prepareDataForJSON() {
  const humain = [];
  for (let id in positions) {
    const color = colors[id];
    const positionsForId = positions[id].filter(p => p.t === time);
    if (positionsForId.length > 0) {
      humain.push({ color, ...positionsForId[0] });
    }
  }
  return { humain };
}

// associer une couleur à chaque identifiant d'individu
for (let i = 0; i < MAX_INDIVIDUS; i++) {
  const color = Math.floor(Math.random() * 16777215).toString(16);
  colors[i] = color.padStart(6, '0');
}

// écouter les données UDP
server.on('error', (err) => {
  console.log(`Erreur du serveur: ${err.stack}`);
  server.close();
});

server.on('message', (msg, rinfo) => {
  try {
    const data = JSON.parse(msg.toString());
    const { x, y, z, t, id } = data;
    if (id < MAX_INDIVIDUS) {
      addPosition(id, x, y, z, t);
    }
  } catch (error) {
    console.log(`Erreur lors de la lecture des données UDP: ${error.message}`);
  }
});

server.on('listening', () => {
  const address = server.address();
  console.log(`Serveur en écoute ${address.address}:${address.port}`);
});

// écrire les données dans un fichier JSON toutes les 0,5 secondes
setInterval(() => {
  const data = prepareDataForJSON();
  const fileName = `data_${time.toFixed(1)}.json`;
  fs.writeFile(fileName, JSON.stringify(data), (err) => {
    if (err) {
      console.log(`Erreur lors de l'écriture du fichier ${fileName}: ${err.message}`);
    }
  });
  time += 0.5;
}, 500);

// démarrer le serveur
server.bind(PORT);
