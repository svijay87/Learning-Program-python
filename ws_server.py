import websockets
import asyncio

class WS_Server():

    def __init__(self : object, host : str ="localhost", port : int =1234):
        self.host = host
        self.port = port


    async def response(self : object, websocket : object, path : str):
        message = await websocket.recv()
        print(f"Received message from client : {message}")
        await websocket.send("We have received your message!")


ws_server_obj = WS_Server()
start_server = websockets.serve(ws_server_obj.response, ws_server_obj.host, ws_server_obj.port)
asyncio.get_event_loop().run_until_complete(start_server)
print('Server is started')
asyncio.get_event_loop().run_forever()

