from socket import *


def socket_control():

    print("Waiting for client connection ..")

    server_socket = socket(AF_INET, SOCK_STREAM)

    server_socket.bind(("192.168.43.34", 50011))
    server_socket.listen(0)

    (client_socket, adress) = server_socket.accept()

    return client_socket, server_socket


if __name__ == '__main__':

    client_socket, server_socket = socket_control()

    while True:

        ans = (str({"4": 1})).encode()
        client_socket.send(ans)
        h = client_socket.recv(1024)
        print(h)

    server_socket.close()
    client_socket.close()
