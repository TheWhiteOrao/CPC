from socket import *
#Blender = Server


print(gethostbyname(gethostname()))
host = "169.254.44.190"
port = 12356

server_socket = socket(AF_INET, SOCK_STREAM)

try:
    server_socket.bind((host, port))
except:
    pass

server_socket.listen(1)

conn, addr = server_socket._accept()

print(addr)
