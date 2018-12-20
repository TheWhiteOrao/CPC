
# ███    ███  █████  ██ ███    ██     ███████ ███████ ██████  ██    ██ ███████ ██████
# ████  ████ ██   ██ ██ ████   ██     ██      ██      ██   ██ ██    ██ ██      ██   ██
# ██ ████ ██ ███████ ██ ██ ██  ██     ███████ █████   ██████  ██    ██ █████   ██████
# ██  ██  ██ ██   ██ ██ ██  ██ ██          ██ ██      ██   ██  ██  ██  ██      ██   ██
# ██      ██ ██   ██ ██ ██   ████     ███████ ███████ ██   ██   ████   ███████ ██   ██

from socket import *
from CPC_RR import *
from CPC_RC import *

Main_Loop = True

while Main_Loop:

    left_x_signal = RC(RR(0), -1, 1)
    left_y_signal = RC(RR(1), -1, 1)
    right_x_signal = RC(RR(2), -1, 1)
    right_y_signal = RC(RR(3), -1, 1)

    print("left_x: %f  " % left_x_signal,
          "left_y: %f  " % left_y_signal,
          "right_x: %f  " % right_x_signal,
          "right_y: %f  " % right_y_signal)
