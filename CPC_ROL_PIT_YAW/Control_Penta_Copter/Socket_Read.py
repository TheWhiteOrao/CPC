from socket import *

# 192.168.43.34

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("192.168.43.34", 50010))

while True:

    msg = client_socket.recv(1024)
    msg = msg.decode()
    print(msg)

client_socket.close()
