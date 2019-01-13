from socket import *

# 192.168.43.34


def socket_connect():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("192.168.43.34", 50010))

    return client_socket


def socket_read(client_socket):
    message = (client_socket.recv(2048)).decode()
    return message


if __name__ == '__main__':

    client_socket = connect()
    while True:
        print(socket_read(client_socket))

    client_socket.close()
