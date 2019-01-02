from time import *
from CPC_DELTA_TIME import delta_time_calculate
from CPC_UNSLEEP import usleep
prev_time = 0

for I in range(100):
    delta_time, prev_time = delta_time_calculate(prev_time)

    print(delta_time, I)

# currenttime = 0
# for I in range(100):
#     previoustime = currenttime
#     currenttime = time_ns()
#
#     dt = (currenttime - previoustime) / 1000000000
#
#     if dt < (1 / 1300):
#         usleep((1 / 1300 - dt) * 1000000)
#         currenttime = time_ns()
#
#     dt = (currenttime - previoustime) / 1000000000
#
#     print(dt, I)
