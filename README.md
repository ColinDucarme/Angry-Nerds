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