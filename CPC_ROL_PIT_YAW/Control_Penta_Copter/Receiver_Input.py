from N2.rcinput import *


# Receiver imput, reads the signal of the transmitter and returns them in a rage of numbers

rc_imput = RCInput()


def receiver_imput(channel_number):

    return int(rc_imput.read(channel_number))


if __name__ == '__main__':

    while True:
        print(receiver_imput(0))
