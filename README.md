# Angry-Nerds

Librairies externes : Mediapipe, Pygame, Websocket

# Pré-requis
Avoir la librairie websocket Pypy v10.4 installée
Mediapipe version 0.9.1.0
Pygame version 2.2.0

# Comment fonctionner ?
Le côté Listener est intégré au jeu en utilisant la fonction de la classe vue dans le fichier server.py, pour le lancer il suffit de lancer le fichier runner.py qui utilisera la classe contenue dans server.py.

# Changer l'adresse ip et le port du listener

Si vous avez besoin de changer l'adresse IP, accédez simplement au fichier server.py et modifiez l'adresse "host", de même pour le port. Parfois, la fonction server.py peut être appelée avant le délai OS "Time_Delay", ce qui entraîne une erreur disant "adresse déjà utilisée". Pour résoudre ce problème, il suffit de changer le port utilisé.

# Règles
Angry-Nerds est un jeu à deux joueurs. L'un a le contrôle de l'oiseau (le angry nerd) dont le but est de monter le plus haut possible. L'autre a pour objectif de l'en empêcher.

La position de l'oiseau sur l'écran suit les déplacements de la main du premier joueur. Il pourra aussi récupérer des pouvoirs, activable par certains mouvements du premier joueur : Poing fermé pour ralentir le temps; Main pointant vers le bas pour rétrécir; Mais en forme de fusils pour tirer.

Le deuxième joueur pourra, par l'intermédiaire d'un smartphone, envoyer des obstacles au premier joueur en les dessinants.
