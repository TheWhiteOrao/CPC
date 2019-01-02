from time import *
from CPC_UNSLEEP import usleep


def delta_time_calculate(previoustime):

    currenttime = time_ns()

    delta_time = (currenttime - previoustime) / 1000000000

    if delta_time < (1 / 1300):
        usleep((1 / 1300 - delta_time) * 1000000)
        currenttime = time_ns()

    delta_time = (currenttime - previoustime) / 1000000000

    return delta_time, currenttime
