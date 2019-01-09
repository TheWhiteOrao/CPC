from N2.rcinput import *


# Receiver imput, reads the signal of the transmitter and returns them in a rage of numbers

rc_imput = RCInput()


def receiver_imput(channel_range):

    if type(channel_range) == tuple:
        imput_dir = {}

        for i in channel_range:
            imput_dir[i] = int(rc_imput.read(i))

        return imput_dir

    if type(channel_range) == int:
        return int(rc_imput.read(channel_range))


if __name__ == '__main__':
    while True:
        print(receiver_imput((0, 1, 2, 3)))
