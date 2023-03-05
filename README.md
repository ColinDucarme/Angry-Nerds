# Angry-Nerds

# Règles
Angry-Nerds est un jeu à deux joueurs. L'un a le contrôle de l'oiseau (le angry nerd) dont le but est de monter le plus haut possible. L'autre a pour objectif de l'en empêcher.

La position de l'oiseau sur l'écran suit les déplacements de la main du premier joueur. Il pourra aussi récupérer des pouvoirs, activable par certains mouvements du premier joueur : Poing fermé pour ralentir le temps; Main pointant vers le bas pour rétrécir; Mais en forme de fusils pour tirer.

Le deuxième joueur pourra, par l'intermédiaire d'un smartphone, envoyer des obstacles au premier joueur en les dessinants.



# Angry-Nerds - Listener

# Pré-requis

*websocket Pypy v10.4 
*Mediapipe version 0.9.1.0
*Pygame version 2.2.0

# Comment fonctionner ?
Le côté Listener est intégré au jeu en utilisant la fonction de la classe vue dans le fichier server.py, pour le lancer il suffit de lancer le fichier runner.py qui utilisera la classe contenue dans server.py.

# Changer l'adresse ip et le port du listener

Si vous avez besoin de changer l'adresse IP, accédez simplement au fichier server.py et modifiez l'adresse "host", de même pour le port. Parfois, la fonction server.py peut être appelée avant le délai OS "Time_Delay", ce qui entraîne une erreur disant "adresse déjà utilisée". Pour résoudre ce problème, il suffit de changer le port utilisé.

# Angry Nerds - Web Interface

## Prerequisites

* Node JS V16.13.0+
* npm V8.1.0+
* vue js version 3
  
## NPM dependencies
* paper 0.12.17
* vue 3.2.45
* vue-router 4.1.6

## How to run ?

The first step is to open a terminal inside of the web interface directory and run the following command to install all the dependencies:
```
npm i
```
And to start the server, please run the following command:
```
npm run dev
```

The command will display two IPs to you, one local (that will only work on your computer), and a "Network" one, that will make the app visible to other devices on the network.

# How to use the webapp ?

Once the game server (python) is up and running, go on the provided IP given previously with a smart phone, and simply click on `play`.

On top of the mobile game screen, you will see your `energy` and a `timer`. The energy is capped to `50`.

Below, you will have the drawing zone. You will be able to draw basically anything you want, but be careful, **drawing consumes energy ! Once you are at 0 energy, you cannot draw anymore**. But do not worry, energy levels slowly come back over time, and you will also gain a bonus of 7 energy when sending a drawing to the other player.

To send a drawing, you will have to click on one of the three buttons below the drawing zone, clicking on the buttons will send the drawing on the computer game on one of the three imaginary columns.
