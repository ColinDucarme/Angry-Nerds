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
            <p>RULES HERE !</p>
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
