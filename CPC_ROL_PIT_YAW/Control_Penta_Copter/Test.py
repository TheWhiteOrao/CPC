
# x = dict(map(lambda x: (x, 0), range(1, 20)))
# print(x)
# h = []
# h.append(1)
# h = {}
# h.

# h = {0: 143, 1: 324634673, 2: 34346, 3: 2332, 4: 235, 5: 45756, 6: 325, 7: 12421, 8: 4211223, 9: 12342311, 10: 8786, 11: 345}
# l = {}
# for i in range(len(h)):
#     l[i] = (h[i] * 2 / 3463)**-0.5
# print(l)
# k1 = (h[0] * 2 / 3463)**-0.5
# k2 = (h[1] * 2 / 3463)**-0.5
# k3 = (h[2] * 2 / 3463)**-0.5
# k4 = (h[3] * 2 / 3463)**-0.5
# k5 = (h[4] * 2 / 3463)**-0.5
# k6 = (h[5] * 2 / 3463)**-0.5
# k7 = (h[6] * 2 / 3463)**-0.5
# k8 = (h[7] * 2 / 3463)**-0.5
# k9 = (h[8] * 2 / 3463)**-0.5
# k10 = (h[9] * 2 / 3463)**-0.5
# k11 = (h[10] * 2 / 3463)**-0.5
# k12 = (h[11] * 2 / 3463)**-0.5
#
#
# print(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12)

# h = {0: 1, 1: 19}
#
# for i in h:
#     print(h[i])

from Receiver_Input import receiver_imput
from Receiver_Signal_Converter import receiver_signal_converter
from time import process_time_ns

h = 0
while True:
    print(receiver_signal_converter(receiver_imput({0: (0, 1), 1: (-1, 1), 2: (-1, 1), 3: (-1, 1)})))
    print(h - process_time_ns())
    h = process_time()
