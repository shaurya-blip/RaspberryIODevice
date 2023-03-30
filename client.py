# Import Libraries

from gpiozero import Button, LED
import time

import socket

# Declare variables

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!q"

SERVER = '192.168.1.111' # Server Address
PORT = 5678 # Server Port
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client.connect(ADDR))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)

    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    recv_msg = client.recv(100000000).decode(FORMAT)

    return recv_msg

# testing function
print(send('hello'))

# Declaring buttons
# Button(GPIO Adress in Raspberry Pi(Not Physical Address))

button_up = Button(17) 
button_down = Button(4)
button_left = Button(3)
button_right = Button(2)
button_clear = Button(27) 

# LED for debugging

led = LED(22)

# A while True which checks the state of the buttons every 500 miliseconds
# If button.value == 1 Then it will send the function of the button to the server
# And as a confirmation the LED will also light up

while True:
    if button_up.value == 1:
        print('UP')
        send('UP')
        led.on()
    if button_down.value == 1:
        print('DOWN')
        send('DOWN')
        led.on()
    if button_left.value == 1:
        print('LEFT')
        send('LEFT')
        led.on()
    if button_right.value == 1:
        print('RIGHT')
        send('RIGHT')
        led.on()
    if button_clear.value == 1:
        print('CLEAR')
        send('clear')
        led.on()
    
    time.sleep(0.5)
    
    led.off()