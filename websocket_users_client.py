import asyncio
import websockets


async def client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as ws:
        message = 'Привет, сервер!'
        await ws.send(message)
        for _ in range(5):
            response = await ws.recv()
            print(response)

asyncio.run(client())