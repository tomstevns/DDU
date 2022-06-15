import socket
import time
HEADER = 64
PORT = 5052
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.101"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def firstMessage():
    send("Hello World!")
    time.sleep(5)

def secondMessage():
    send("second message!")
    time.sleep(5)

def terminatingMessage():
    send("Good bye - That's all folks!")
    time.sleep(5)
    send(DISCONNECT_MESSAGE)

firstMessage()
secondMessage()
terminatingMessage()




