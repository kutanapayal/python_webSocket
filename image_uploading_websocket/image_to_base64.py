from websocket import create_connection
import base64
ws = create_connection("ws://echo.websocket.org/")

img_path=input('Enter image path to upload::')

with open(img_path, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)


print("Sending 'image base64'...")    
ws.send(base64_encoded_data)
print("Sent")

print("Receiving...")
result =  ws.recv()
print("Received " , result)
ws.close()
