from time import sleep

# Microsecond sleep time
# x are in seconds and while convert to microsecond


def micro_sleep(x):
    return sleep(x * 0.000001)


if __name__ == '__main__':
    micro_sleep(100)
