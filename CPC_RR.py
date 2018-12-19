
# ██████  ███████  █████  ██████      ██████  ███████  ██████ ███████ ██ ██    ██ ███████ ██████
# ██   ██ ██      ██   ██ ██   ██     ██   ██ ██      ██      ██      ██ ██    ██ ██      ██   ██
# ██████  █████   ███████ ██   ██     ██████  █████   ██      █████   ██ ██    ██ █████   ██████
# ██   ██ ██      ██   ██ ██   ██     ██   ██ ██      ██      ██      ██  ██  ██  ██      ██   ██
# ██   ██ ███████ ██   ██ ██████      ██   ██ ███████  ██████ ███████ ██   ████   ███████ ██   ██

from sys import *
from time import *

from CPC_NAVIO2.rcinput import *
from CPC_NAVIO2.util import *

check_apm()

receiver_imput = RCInput()


def receiver_channel(channel_number):
    return receiver_imput.read(channel_number)
