# Import libraries

import socket
import threading
import turtle

# Create a turtle object

t = turtle.Turtle()
t.color('yellow')
t.screen.bgcolor('orange')

# Set socket variables

SERVER = '192.168.1.111'

clients = []
HEADER = 64
PORT = 5678
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!q"

# Create server socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Handle client connections

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr[0]}:{addr[1]} connected")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            # print(msg_length)
            msg_length = int(msg_length)
            msg = conn.recv(int(100000000)).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr[0]}:{addr[1]}] has disconnected")
                # conn.send("You have been disconnected".encode(FORMAT))
            
            if msg == 'clear':
                print(f'[{addr[1]}] The client has ordered to wipe the board!')
            else:
                print(f"[{addr[1]}] The client has ordered to move the turtle {msg}")
            
            # If message is UP, DOWN, LEFT, RIGHT, clear, then move the turtle 
            # accordingly
            
            if msg == "UP":
                t.forward(100)
            elif msg == "DOWN":
                t.backward(100)
            elif msg == "LEFT":
                t.left(90)
            elif msg == "RIGHT":
                t.right(90)
            elif msg == "clear":
                t.clear()
            else:
                pass
            
            # Send something back to the client
            
            conn.send(f"200 - {msg}".encode(FORMAT))

    conn.close()

# Start the server

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        
        handle_client(conn,addr)


def startserver():
    print(f"[STARTING] SERVER is starting on {str(SERVER)}:{str(PORT)}")
    print(f"[RUNNING] Server is succesfully running....")
    start()


print("______________________________________________________")
startserver()
