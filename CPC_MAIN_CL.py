
# ███    ███  █████  ██ ███    ██      ██████ ██      ██ ███████ ███    ██ ████████
# ████  ████ ██   ██ ██ ████   ██     ██      ██      ██ ██      ████   ██    ██
# ██ ████ ██ ███████ ██ ██ ██  ██     ██      ██      ██ █████   ██ ██  ██    ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██      ██ ██      ██  ██ ██    ██
# ██      ██ ██   ██ ██ ██   ████      ██████ ███████ ██ ███████ ██   ████    ██

from socket import *

main_cl = socket(AF_INET, SOCK_STREAM)

main_cl_addr = ("192.168.43.34", 35467)
main_cl.connect(main_cl_addr)

while True:
    print(main_cl.recv)
