import socket
from art import *
import sys
import time
#port numbers available : 1900, 62434

s = socket.socket()
host = socket.gethostname()
tprint("WELCOME")
print("Server will start on host: ", host)
port = 62434
s.bind((host,port))
print("")
print("Server done binding to host and port sucessfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, "Has connected to the server and is now online...")
print("")
while 1:
    message = input(str(">>> "))
    message = message.encode()
    conn.send(message)
    print("message sent...")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client: ", incoming_message)
    print()