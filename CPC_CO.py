
#  ██████  ██████  ███████ ██ ███    ██ ██    ██ ███████
# ██      ██    ██ ██      ██ ████   ██ ██    ██ ██
# ██      ██    ██ ███████ ██ ██ ██  ██ ██    ██ ███████
# ██      ██    ██      ██ ██ ██  ██ ██ ██    ██      ██
#  ██████  ██████  ███████ ██ ██   ████  ██████  ███████

from CPC_FR import *

pi = 3.141592653589


def CO(cos_input):

    cos_deg = (cos_input * pi) / 180
    cos_result = 1

    for i in range(1, 50):

        cos_call = (cos_deg ** (2 * i)) / FR(2 * i)
        sign_changer = (-1)**(i)
        cos_result += cos_call * sign_changer

    return round(cos_result, 10)


if __name__ == '__main__':
    print(CO(45))
