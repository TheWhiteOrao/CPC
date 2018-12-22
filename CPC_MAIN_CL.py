
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
    k = main_cl.recv(1024).decode()
    left_x_signal = k[0]
    left_y_signal = k[1]
    right_x_signal = k[2]
    right_y_signal = k[3]

    print("left_x: %f  " % left_x_signal,
          "left_y: %f  " % left_y_signal,
          "right_x: %f  " % right_x_signal,
          "right_y: %f  " % right_y_signal)
