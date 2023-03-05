<script>

export default {
    mounted(){
        window.addEventListener('scroll', e => {
            e.preventDefault();
        })
    }
}

</script>

<template>
    <div id="main-menu-container">
        <div id="game-title">
            <p>Angry Nerds<br>-<br>The Game</p>
        </div>
        <div id="menu-container">
            <router-link class="menu-button" to="/game">Start</router-link>
            <router-link class="menu-button" to="/rules">Rules</router-link>
        </div>
        <img id="image-oiseau" src="/images/bird.png"/>
    </div>

    



</template>

<style scoped>
    #main-menu-container {
        position: relative;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        /* justiffont-family: 'Press Start 2P', cursive;y-content: center; */
        font-family: 'Press Start 2P', cursive;
        align-items: center;
        overflow: hidden;
    }
    p {
        /* font-size: 3em; */
        font-size: 32px;
        text-align: center;
        line-height: 0.75;
        color: white;
    }
    #game-title {
        margin-top: 0;
        /* background-color: rgb(146, 93, 7); */
        background-image: url("images/sign-texture.jpeg");
        background-size: auto;
        background-repeat: repeat;
        /* background-position: center; */
        padding: 15px;
        width: 100%;
        /* font-family: 'Press Start 2P', cursive; */
/* font-family: 'VT323', monospace; */
font-family: 'Press Start 2P', cursive;
        font-size: 10px;
    }
    #menu-container {
        padding-top: 128px;
        flex: 1;
        background-color: rgb(221, 238, 255);
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
        overflow-y: hidden;
    }
    .menu-button {
        color: white;
        font-size: 2em;
        padding: 15px;
        margin: 15px;
        text-decoration: none;
        border-radius: 5px;
        width: 50%;
        text-align: center;
        z-index: 2000;
        background-image: url("images/sign-texture.jpeg");
        background-size: auto;
        background-repeat: repeat;
        font-family: 'Press Start 2P', cursive;
    }
    #image-oiseau {
        position: absolute;
        bottom: 0;
        left: 0;
        margin-left: 100px;
        margin-bottom: -150px;
        rotate: -45deg;
        /* z-index: 0; */
    }
</style>
