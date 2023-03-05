import json
import asyncio
import websockets


class ObstaclesJSON:

    def __init__(self, col, svg, Xmin, Xmax, Ymin, Ymax, change=False, connected=False):
        self.col = col
        self.svg = svg
        self.Xmin = Xmin
        self.Xmax = Xmax
        self.Ymin = Ymin
        self.Ymax = Ymax
        self.change = change
        self.connected = connected


class Socket:

    def __init__(self):
        self.obs = ObstaclesJSON(None, None, None, None, None, None)

    async def receive_data(self, websocket):
        print("Client connected")
        self.obs.connected=True
        json_data = None
        try:
            async for data in websocket:
                print('Received:', data)
                json_data = json.loads(data)
                self.obs.col = json_data['col']
                self.obs.svg = json_data['svg']
                self.obs.Xmax = json_data['maxX']
                self.obs.Xmin = json_data['minX']
                self.obs.Ymax = json_data['maxY']
                self.obs.Ymin = json_data['minY']
                self.obs.change = True

        except json.JSONDecodeError as e:
            print('Error decoding JSON:', e)
        finally:
            print("Client disconnected")
            self.obs.connected = False

    async def main(self):
        async with websockets.serve(self.receive_data, '192.168.58.139', 8888):
            print('Listening on host:8888...')
            await asyncio.Future()  # run forever

    def run(self):
        asyncio.run(self.main())
