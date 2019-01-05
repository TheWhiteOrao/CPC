from time import sleep


# Microsecond sleep time
# seconds  while convert to microsecond

def micro_sleep(seconds):
    return sleep(seconds * 0.000001)


if __name__ == '__main__':
    micro_sleep(100)
