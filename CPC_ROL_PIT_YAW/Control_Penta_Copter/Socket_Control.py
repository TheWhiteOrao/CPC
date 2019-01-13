from socket import *


def socket_control():

    print("Waiting for client connection ..")

    server_socket = socket(AF_INET, SOCK_STREAM)

    server_socket.bind(("192.168.43.34", 50010))
    server_socket.listen(0)

    (client_socket, adress) = server_socket.accept()

    return client_socket


lol = socket_control()
while True:

    ans = str({"4": 1})

    ans = ans.encode()
    lol.send(ans)

server_socket.close()
client_socket.close()
