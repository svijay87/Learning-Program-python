import websockets
import asyncio

class WSClient:

    def __init__(self):
        self.ws_server = "ws://simple-websocket-server-echo.glitch.me/"

    async def listen(self):

        async with websockets.connect(self.ws_server) as ws:
            try:
                while True:
                    msg = await ws.recv()
                    print(msg)
            except KeyboardInterrupt:
                print('Client closing')
                ws.close()


wsclient_obj = WSClient()
asyncio.get_event_loop().run_until_complete(wsclient_obj.listen())