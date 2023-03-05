<script>
import paper from "paper";

export default {
    data(){
        return {
            energy: 50,
            timer: 0,
            lePapier: null,
            minX: 0,
            maxX: 0,
            minY: 0,
            maxY: 0
        }
    },
    mounted(){
        let start_game_data = {
            start_game: true
        }

        const s_socket = new WebSocket("ws://192.168.58.139:8888");
            s_socket.onopen = async function(event) {
                s_socket.send(JSON.stringify(start_game_data));
            };

        const canvas = this.$refs.drawZone;
        const infoZone = this.$refs.infoZone;
        const clientHeight = document.body.clientHeight;

        infoZone.style.height = clientHeight/8 + "px";
        canvas.width = document.body.clientWidth;
        canvas.height = clientHeight/3;

        const paperScope = new paper.PaperScope();
        paperScope.setup(canvas);
        this.lePapier = paperScope;

        this.timerManager();
        this.incrementEnergy();

        let path;

        canvas.addEventListener('mousedown', (event) => {
        path = new this.lePapier.Path({
            strokeColor: 'red',
            strokeWidth: 30,
            fill: none
        });
        path.add(new paper.Point(event.offsetX, event.offsetY));
        this.minX = event.offsetX;
        this.maxX = event.offsetX;
        this.minY = event.offsetY;
        this.maxY = event.offsetY;
        });

        canvas.addEventListener('mousemove', (event) => {
        if (path && this.energy > 0) {
            path.add(new paper.Point(event.offsetX, event.offsetY));
            this.energy -= 1;
            this.lePapier.view.draw();
            if(event.offsetX < this.minX) this.minX = event.offsetX;
            if(event.offsetX > this.maxX) this.maxX = event.offsetX;
            if(event.offsetY < this.minY) this.minY = event.offsetY;
            if(event.offsetX > this.maxY) this.maxY = event.offsetY;
        }
        });

        canvas.addEventListener('mouseup', () => {
        path.simplify(10);
        path = null;
        });

        canvas.addEventListener('touchstart', (event) => {
        event.preventDefault();
        path = new this.lePapier.Path({
            strokeColor: 'black',
            strokeWidth: 3,
        });
        path.add(new paper.Point(event.touches[0].clientX, event.touches[0].clientY - clientHeight/8));
        this.minX = event.touches[0].clientX;
        this.maxX = event.touches[0].clientX;
        this.minY = event.touches[0].clientY;
        this.maxY = event.touches[0].clientY;
        });

        canvas.addEventListener('touchmove', (event) => {
        event.preventDefault();
        if (path && this.energy > 0) {
            path.add(new paper.Point(event.touches[0].clientX, event.touches[0].clientY - clientHeight/8));
            this.lePapier.view.draw();
            this.energy -= 0.75;
            if(event.touches[0].clientX < this.minX) this.minX = event.touches[0].clientX;
            if(event.touches[0].clientX > this.maxX) this.maxX = event.touches[0].clientX;
            if(event.touches[0].clientY < this.minY) this.minY = event.touches[0].clientY;
            if(event.touches[0].clientY > this.maxY) this.maxY = event.touches[0].clientY;
        }
        });

        canvas.addEventListener('touchend', (event) => {
        event.preventDefault();
        path.simplify(10);
        path = null;
        });
    },
    methods: {
        clearCanvas(){
            let layer = this.lePapier.project.activeLayer;

            for(let n = layer.children.length - 1; n >= 0; n--){
                layer.children[n].remove();
            }

            this.lePapier.view.update();
        },
        canvasToCSV(){
            // if(!paper.project) return;
            let svg = this.lePapier.project.exportSVG({asString: true});
            let newSVG = svg.replace(/"/g, "'");
            return newSVG;
        },
        sendToServer(col){
            if(this.lePapier.project.layers.length == 0) return;
            let svg = this.canvasToCSV();
            console.log(svg);
            this.clearCanvas();
            // console.log(this.minX, this.maxX);
            
            let data = {
                svg: svg,
                col: col,
                maxX: this.maxX,
                minX: this.minX,
                maxY: (this.maxY - document.body.clientHeight/8),
                minY: (this.minY - document.body.clientHeight/8),
            };

            const socket = new WebSocket('ws://192.168.58.139:8888');
            socket.onopen = async function(event) {
                socket.send(JSON.stringify(data));
            };
            // add bonus energy for sending drawing
            this.energy += 7;
            this.spawnDrawing(svg, col);
        },
        async timerManager(){
            setInterval(() => {
                this.timer++;
            }, 1000);
        },
        async incrementEnergy(){
            setInterval(() => {
                if(this.energy < 49) this.energy++
            }, 300);
        },
        spawnDrawing(svg, col){
            console.log(svg);
            let id = "col-" + col;
            var element = document.getElementById(id);
            var rect = element.getBoundingClientRect();

            var x = rect.left;
            var y = rect.top;
            console.log('x: ' + x, "y: " + y);
            let imgDiv = document.createElement('div');
            imgDiv.style.width = (this.maxX - this.minX) + "px";
            imgDiv.style.height = (this.maxY - this.minY) + "px";
            imgDiv.style.position = "absolute";
            imgDiv.style.zIndex = 1;
            imgDiv.style.top = y;
            imgDiv.style.marginLeft = x + "px";

            // imgDiv.innerHTML = svg;

            let img = new Image();
            img.src = "data:image/svg+xml;base64," + btoa(svg);
            // img.style.width = "150%";
            img.style.marginLeft = ("-" + this.minX + "px");
            img.style.marginTop = -this.minY + "px";
            img.style.position = "relative";
            imgDiv.appendChild(img);

            document.getElementById('game-container').appendChild(imgDiv);
            this.goDownSVG(imgDiv);
        },
        async goDownSVG(element){
            let move = true;
                setInterval(() => {
                        var rect = element.getBoundingClientRect();
                    var x = rect.left;
                    var y = rect.top;
                    if(y >= document.body.clientHeight + 200){
                        element.remove();
                        move = false;
                        return;
                    }
                    element.style.top = (y + 1) + "px";
                }, 1);

        }
    }
}

</script>

<template>
    <div id="game-container">
        <div id="info-zone" ref="infoZone">
        <div id="energy-zone">
            <p>
                ENERGY {{ Math.round(energy) }}
            </p>
        </div>
        <div id="timer-zone">
            TIMER {{ timer }}
        </div>
    </div>
    <div id="draw-zone" style="width: 100%;">
        <canvas ref="drawZone"></canvas>
    </div>
    <div id="button-zone">
        <button @click="sendToServer(1)">1</button>
        <button @click="sendToServer(2)">2</button>
        <button @click="sendToServer(3)">3</button>
    </div>
    <img src="/images/cloud-pipes.png" id="cloud-pipes-img"/>
    <div id="drawing-spitter">
        <div class="pipe-col" id="col-1"></div>
        <div class="pipe-col" id="col-2"></div>
        <div class="pipe-col" id="col-3"></div>
    </div>
    </div>
</template>

<style scoped>
    canvas {
        background-color: white;
    }
    #info-zone {
        color: white;
        width: 100%;
        background-image: url("/images/sign-texture.jpeg");
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 24px;
        font-family: 'Press Start 2P', cursive;

    }
    #button-zone {
        border: 1px solid green;
        width: 100%;
        display: flex;
        justify-content: stretch;
        align-items: stretch;
    }
    button {
        flex: 1;
        z-index: 999;
    }
    #energy-zone {
        margin-left: 8px;
    }
    #timer-zone {
        margin-right: 8px;
    }
    #cloud-pipes-img {
        position: relative;
        width: 100%;
        z-index: 15;
    }
    #game-container {
        background-color: aliceblue;
        height: 100%;
    }
    #drawing-spitter {
        width: 100%;
        display: flex;
        justify-content: space-evenly;
    }
    .pipe-col {
        width: 50px;
        height: 50px;
        margin-top: -50px;
    }
</style>
