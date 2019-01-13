
from socket import *

socket_control_penta_copter = socket(AF_INET, SOCK_STREAM)

IP_server = ("192.168.43.34", 12356)
socket_control_penta_copter.connect(IP_server)

print("run")
while True:

    try:
        print(socket_control_penta_copter.recv(2048))
    except:
        pass
