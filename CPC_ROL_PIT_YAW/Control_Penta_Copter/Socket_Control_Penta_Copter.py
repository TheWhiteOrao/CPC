from socket import *

socket_control_penta_copter = socket(AF_INET, SOCK_STREAM)

IP_server = ("169.254.44.190", 12356)
socket_control_penta_copter.connect(IP_server)


while True:
    print("run")
243
