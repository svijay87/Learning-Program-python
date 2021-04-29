import websockets
import asyncio


async def message():

    async with websockets.connect("ws://localhost:1234") as socket:
        while True:
            msg = input("Push message for server")
            await socket.send(msg)
            print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())