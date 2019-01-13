from socket import *

socket_control_penta_copter = socket(AF_INET, SOCK_STREAM)

IP_server = ("192.168.43.243", 46598)
socket_control_penta_copter.connect(IP_server)

H = str({"H": 1})

while True:
    print("run")
    socket_control_penta_copter.send(bytes(H, "utf8"))
