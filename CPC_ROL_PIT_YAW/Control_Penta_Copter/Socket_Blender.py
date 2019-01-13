from socket import *

socket_blender = socket(AF_INET, SOCK_STREAM)


# print(gethostbyname(gethostname()))
IP_server = ("192.168.43.243", 46598)
socket_blender.bind(IP_server)
socket_blender.listen(1)

while True:
    print("run")
    try:
        (socket_control_penta_copter, IP_client) = socket_blender._accept()
        msg = eval(str(socket_control_penta_copter.recv(1024)))

    except:
        pass

    print(msg)
