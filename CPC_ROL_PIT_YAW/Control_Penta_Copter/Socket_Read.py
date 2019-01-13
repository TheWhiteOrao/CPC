from socket import *


def socket_connect():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("192.168.43.34", 50011))

    return client_socket


def socket_read(client_socket):
    message = client_socket.recv(2048)
    client_socket.send((True).encode())
    return message.decode()


if __name__ == '__main__':
    from time import sleep
    client_socket = socket_connect()

    while True:
        Quaternion = (socket_read(client_socket))
        print(Quaternion)

        # print("QuaternionR: %-26s" % Quaternion["QuaternionR"],
        #       "QuaternionI: %-26s" % Quaternion["QuaternionI"],
        #       "QuaternionJ: %-26s" % Quaternion["QuaternionJ"],
        #       "QuaternionK: %-26s" % Quaternion["QuaternionK"])

    client_socket.close()
