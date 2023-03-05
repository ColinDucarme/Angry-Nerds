<script>

export default {
}

</script>

<template>
    <div id="test">
        <div id="title-container">
            <h1>Rules</h1>
        </div>
        <div id="rules-container"> 
            <h2>How to play on the phone ?</h2>
            <p>
Once the game server (python) is up and running, go on the provided IP given previously with a smart phone, and simply click on `play`.

On top of the mobile game screen, you will see your `energy` and a `timer`. The energy is capped to `50`.

Below, you will have the drawing zone. You will be able to draw basically anything you want, but be careful, **drawing consumes energy ! Once you are at 0 energy, you cannot draw anymore**. But do not worry, energy levels slowly come back over time, and you will also gain a bonus of 7 energy when sending a drawing to the other player.

To send a drawing, you will have to click on one of the three buttons below the drawing zone, clicking on the buttons will send the drawing on the computer game on one of the three imaginary columns.

            </p>
<h2>How to play with the hand ? (second player)</h2>
Angry-Nerds est un jeu à deux joueurs. L'un a le contrôle de l'oiseau (le angry nerd) dont le but est de monter le plus haut possible. L'autre a pour objectif de l'en empêcher.

La position de l'oiseau sur l'écran suit les déplacements de la main du premier joueur. Il pourra aussi récupérer des pouvoirs, activable par certains mouvements du premier joueur : Poing fermé pour ralentir le temps; Main pointant vers le bas pour rétrécir; Mais en forme de fusils pour tirer.

Le deuxième joueur pourra, par l'intermédiaire d'un smartphone, envoyer des obstacles au premier joueur en les dessinants.

        </div>
        <div id="bottom-button-container">
            <div>

            </div>
            <router-link id="menu-button" to="/">Menu</router-link>
        </div>
    </div>
</template>

<style scoped>
    #title-container {
        color: white;
        padding: 8px;
        text-align: center;
        background-image: url("images/sign-texture.jpeg");
        background-size: auto;
        background-repeat: repeat;
        font-family: 'Press Start 2P', cursive;
    }
    #bottom-button-container {
        position: absolute;
        bottom: 0;
        width: 100%;
        text-align: center;
        margin-bottom: 32px;
    }
    #menu-button {
        font-size: xx-large;
        padding: 25px;
        color: white;
        padding: 8px;
        border-radius: 8px;
        background-image: url("images/sign-texture.jpeg");
        background-size: auto;
        background-repeat: repeat;
        font-family: 'Press Start 2P', cursive;
    }
    #rules-container {
        overflow-y: scroll;
    }
    #test {
        height: 100%;
        overflow: auto;
    }
</style>
