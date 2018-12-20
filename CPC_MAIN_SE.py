
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

    left_x_signal = RC(RR(0))
    left_y_signal = RC(RR(1))
    right_x_signal = RC(RR(2))
    right_y_signal = RC(RR(3))

    print("left_x: %  " % left_x_signal,
          "left_y: %  " % left_y_signal,
          "right_x: %  " % right_x_signal,
          "right_y: %  " % right_y_signal)
