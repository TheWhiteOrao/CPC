from time import sleep


# Microsecond sleep, will converter seconds to microsecond and return the sleep command in microsecond.

def micro_sleep(seconds):
    return sleep(seconds * 0.000001)


if __name__ == '__main__':

    micro_sleep(100)
