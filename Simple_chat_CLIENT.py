import socket
from art import *
import sys
import time
#port numbers available : 1900, 62434

s = socket.socket()
host = input(str("Please enter the hostname of the server: "))
port = 62434
s.connect((host,port))
print("Connected to server!!!")
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ", incoming_message)
    print("")
    message = input(str(">>> "))
    message = message.encode()
    s.send(message)
    print("message has sent...")
    print("")