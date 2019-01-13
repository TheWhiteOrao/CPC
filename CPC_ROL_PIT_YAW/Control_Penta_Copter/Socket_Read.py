from socket import *
from math import *
from mathutils import *
import bpy


def socket_connect():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("192.168.43.34", 50011))

    return client_socket


def socket_read(client_socket):
    message = client_socket.recv(2048)
    client_socket.send(("True").encode())
    return message.decode()


if __name__ == '__main__':
    from time import sleep
    client_socket = socket_connect()

    while True:
        Quaternion = eval(socket_read(client_socket))

        bpy.context.object.rotation_quaternion[0] = Quaternion["QuaternionR"]
        bpy.context.object.rotation_quaternion[1] = Quaternion["QuaternionI"]
        bpy.context.object.rotation_quaternion[2] = Quaternion["QuaternionJ"]
        bpy.context.object.rotation_quaternion[3] = Quaternion["QuaternionK"]

        sleep(1)

        # print("QuaternionR: %-26s" % Quaternion["QuaternionR"],
        #     "QuaternionI: %-26s" % Quaternion["QuaternionI"],
        #    "QuaternionJ: %-26s" % Quaternion["QuaternionJ"],
        #   "QuaternionK: %-26s" % Quaternion["QuaternionK"])
