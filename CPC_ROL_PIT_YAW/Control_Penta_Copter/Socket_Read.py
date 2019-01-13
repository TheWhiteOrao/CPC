from socket import *


def socket_connect():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("192.168.43.34", 50010))

    return client_socket


def socket_read(client_socket):
    message = (client_socket.recv(2048)).decode()
    return message


if __name__ == '__main__':

    client_socket = socket_connect()

    while True:
        Quaternion = eval(socket_read(client_socket))

        print("QuaternionR: %-26s" % Quaternion["QuaternionR"],
              "QuaternionI: %-26s" % Quaternion["QuaternionI"],
              "QuaternionJ: %-26s" % Quaternion["QuaternionJ"],
              "QuaternionK: %-26s" % Quaternion["QuaternionK"])

    client_socket.close()
