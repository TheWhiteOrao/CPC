from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(("192.168.43.34", 50010))
server_socket.listen(0)

(client_socket, adress) = server_socket.accept()
print("client connected")

while True:
    # msg = client_socket.recv(1024)
    # msg = msg.decode()
    # print(msg)

    ans = str({"4": 1})
    ans = ans.encode()
    client_socket.send(ans)

server_socket.close()
client_socket.close()
