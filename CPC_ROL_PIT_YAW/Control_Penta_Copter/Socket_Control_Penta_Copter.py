from socket import *

socket_control_penta_copter = socket(AF_INET, SOCK_STREAM)

IP_server = ("192.168.43.34", 12345)
socket_control_penta_copter.connect(IP_server)


while True:
    print("run")
