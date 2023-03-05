# Angry-Nerds

# Règles
Angry-Nerds est un jeu à deux joueurs. L'un a le contrôle de l'oiseau (le angry nerd) dont le but est de monter le plus haut possible. L'autre a pour objectif de l'en empêcher.

La position de l'oiseau sur l'écran suit les déplacements de la main du premier joueur. Il pourra aussi récupérer des pouvoirs, activable par certains mouvements du premier joueur : Poing fermé pour ralentir le temps; Main pointant vers le bas pour rétrécir; Mais en forme de fusils pour tirer.

Le deuxième joueur pourra, par l'intermédiaire d'un smartphone, envoyer des obstacles au premier joueur en les dessinants.



# Angry-Nerds - Listener

## Pré-requis

* websocket Pypy v10.4 
* Mediapipe version 0.9.1.0
* Pygame version 2.2.0

## Comment fonctionner ?
Le côté Listener est intégré au jeu en utilisant la fonction de la classe vue dans le fichier server.py, pour le lancer il suffit de lancer le fichier runner.py qui utilisera la classe contenue dans server.py.

## Changer l'adresse ip et le port du listener

Si vous avez besoin de changer l'adresse IP, accédez simplement au fichier server.py et modifiez l'adresse "host", de même pour le port. Parfois, la fonction server.py peut être appelée avant le délai OS "Time_Delay", ce qui entraîne une erreur disant "adresse déjà utilisée". Pour résoudre ce problème, il suffit de changer le port utilisé.

# Angry Nerds - Web Interface

## Pré-requis

* Node JS V16.13.0+
* npm V8.1.0+
* vue js version 3
  
## NPM dependencies
* paper 0.12.17
* vue 3.2.45
* vue-router 4.1.6

## Comment exécuter ?

La première étape est d'ouvrir un terminal dans le répertoire de l'interface web et de lancer la commande suivante pour installer toutes les dépendances :
```
npm i
```
Et pour démarrer le serveur, veuillez exécuter la commande suivante :
```
npm run dev
```

La commande vous affichera deux IPs, une locale (qui ne fonctionnera que sur votre ordinateur), et une "Network", qui rendra l'application visible aux autres appareils du réseau.

# Comment utiliser la webapp ?

Une fois que le serveur de jeu (python) est opérationnel, allez sur l'IP fournie précédemment avec un smartphone, et cliquez simplement sur "Play".

En haut de l'écran du jeu mobile, vous verrez votre `energie` et un `timer`. L'énergie est plafonnée à 50.

En dessous, vous aurez la zone de dessin. Vous pourrez dessiner pratiquement tout ce que vous voulez, mais attention, **dessiner consomme de l'énergie ! Une fois que vous êtes à 0 énergie, vous ne pouvez plus dessiner**. Mais ne vous inquiétez pas, les niveaux d'énergie reviennent lentement avec le temps, et vous gagnerez également un bonus de 7 énergies lorsque vous enverrez un dessin à l'autre joueur.

Pour envoyer un dessin, vous devrez cliquer sur l'un des trois boutons situés en dessous de la zone de dessin. En cliquant sur les boutons, le dessin sera envoyé sur l'ordinateur du jeu sur l'une des trois colonnes imaginaires.

## OS
Fonctionne sur tous les OS
