#!/usr/bin/env python
# WS client example
import base64
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        img_path = input("Enter Image Path :: ")

        with open(img_path, "rb") as image_file:
            data = base64.b64encode(image_file.read())
            
            #base64_img_bytes = base64_encoded_data.decode('utf-8')

        await websocket.send(data)

        server_msg = await websocket.recv()
        print(f"<Message From Server : {server_msg}")

asyncio.get_event_loop().run_until_complete(hello())

# import asyncio
# import pathlib
# import ssl
# import websockets

#  ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#  localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
#  ssl_context.load_verify_locations(localhost_pem)

# async def hello():
#     uri = "wss://localhost:8765"
#     async with websockets.connect(
#         uri 
#         #ssl=ssl_context
#     ) as websocket:
#         name = input("What's your name? ")

#         await websocket.send(name)
#         print(f"> {name}")

#         greeting = await websocket.recv()
#         print(f"< {greeting}")

# asyncio.get_event_loop().run_until_complete(hello())