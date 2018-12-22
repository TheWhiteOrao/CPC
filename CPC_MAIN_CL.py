
# ███    ███  █████  ██ ███    ██      ██████ ██      ██ ███████ ███    ██ ████████
# ████  ████ ██   ██ ██ ████   ██     ██      ██      ██ ██      ████   ██    ██
# ██ ████ ██ ███████ ██ ██ ██  ██     ██      ██      ██ █████   ██ ██  ██    ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██      ██ ██      ██  ██ ██    ██
# ██      ██ ██   ██ ██ ██   ████      ██████ ███████ ██ ███████ ██   ████    ██

from socket import *
from pickle import *

main_cl = socket(AF_INET, SOCK_STREAM)

main_cl_addr = ("192.168.43.34", 35467)
main_cl.connect(main_cl_addr)

while True:
    all = main_cl.recv(512)
    print(all)
    all = loads(all)

    print(all)
