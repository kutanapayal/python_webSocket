#!/usr/bin/env python

# WS server example
from PIL import Image
from io import BytesIO
import base64
import os
import asyncio
import websockets

async def hello(websocket, path):
    
    base64_encoded_data = await websocket.recv()
    print(f"< {base64_encoded_data}")

    try:
        os.mkdir("uploaded_images")
        print(os.getcwd())
    except Exception as e:
        print(e)

    img_num=1
    for i in os.listdir(os.getcwd()+"/uploaded_images"):
        img_num+=1
    file_name=os.getcwd()+"/uploaded_images/"+"img_"+str(img_num)+".png"
    
    send_msg="None..."
    try:
        # #base64_encoded_data = base64_encoded_data.encode('utf-8')
        # im = Image.open(BytesIO(base64.b64decode(base64_encoded_data)))
        # im.save(file_name, 'PNG')
        with open(file_name,'wb+') as f:
            decoded_image_data = base64.decodebytes(base64_encoded_data)
            f.write(decoded_image_data)
        send_msg="Image Uploaded Successfully."

    except Exception as e:
        print(e)
        send_msg="sorry,image is not uploaded."    
    
    await websocket.send(send_msg)
    print(f"> {send_msg}")

print(f"< Waiting For Client...")
start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# WSS (WS over TLS) server example, with a self-signed certificate

# import asyncio
# import pathlib
# import ssl
# import websockets

# async def hello(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")

#     greeting = f"Hello {name}!"

#     await websocket.send(greeting)
#     print(f"> {greeting}")

#  ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#  localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
#  ssl_context.load_cert_chain(localhost_pem)

# start_server = websockets.serve(
#     hello, "localhost", 8765
#     # ssl=ssl_context
# )

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()