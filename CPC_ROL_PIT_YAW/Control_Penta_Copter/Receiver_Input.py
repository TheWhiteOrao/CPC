from N2.rcinput import *


# Receiver imput, reads the signal of the transmitter and returns them in a rage of numbers

rc_imput = RCInput()


def receiver_imput(channel_range):

    imput_dir = {}

    for i in channel_range:
        imput_dir[i] = int(rc_imput.read(i)), channel_range[i]

    print(imput_dir)


if __name__ == '__main__':
    while True:
        print(receiver_imput({0: (0, 1), 1: (-1, 1), 2: (-1, 1), 3: (-1, 1)}))
