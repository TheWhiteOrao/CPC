
# ██████  ███████  █████  ██████      ██████  ███████  ██████ ███████ ██ ██    ██ ███████ ██████
# ██   ██ ██      ██   ██ ██   ██     ██   ██ ██      ██      ██      ██ ██    ██ ██      ██   ██
# ██████  █████   ███████ ██   ██     ██████  █████   ██      █████   ██ ██    ██ █████   ██████
# ██   ██ ██      ██   ██ ██   ██     ██   ██ ██      ██      ██      ██  ██  ██  ██      ██   ██
# ██   ██ ███████ ██   ██ ██████      ██   ██ ███████  ██████ ███████ ██   ████   ███████ ██   ██

from CPC_NAVIO2.rcinput import *
from CPC_NAVIO2.util import *

check_apm()

receiver_imput = RCInput()


def RR(channel_number):
    return receiver_imput.read(channel_number)
