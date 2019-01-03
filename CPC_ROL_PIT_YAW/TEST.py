# from time import *
# from CPC_DELTA_TIME import delta_time_calculate
# from CPC_UNSLEEP import usleep
# prev_time = 0
#
# for I in range(100):
#     delta_time, prev_time = delta_time_calculate(prev_time)
#
#     print(delta_time, I)

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

# print((2 * 2) ** -0.5)
# print(4 ** 0.5)


# l = 0
#
#
# def lol():
#     global l
#     for i in range(4):
#         l += 1
#
#
# g = 1
# s = 1
# k = 1
# m = 1
#
#
# def test(g,
#          s,
#          k,
#          m):
#     k = l + l
#     return k
#
#
# print(lol(), l)
# print(test(g, s, k, m))
# print(0 / 1)

def converter(raw_imput, offset_imput, raw_output_lowest, raw_output_highest):
    set_output_lowest = raw_output_lowest - offset_imput
    set_output_highest = raw_output_highest - offset_imput

    # print(set_output_lowest, set_output_highest, raw_output_lowest, raw_output_highest)

    set_output_range = raw_output_highest - raw_output_lowest

    if set_output_lowest + offset_imput * 2 < raw_imput and set_output_highest + offset_imput * 2 > raw_imput:
        return (((set_output_highest - set_output_lowest) / set_output_range) * (set_output_range - (raw_output_highest - raw_imput))) + set_output_lowest

    elif set_output_lowest + offset_imput * 2 <= raw_imput and set_output_highest + offset_imput * 2 <= raw_imput:
        return set_output_lowest - (raw_output_highest - raw_imput)
    else:
        return set_output_highest + (raw_output_highest + raw_imput)


if __name__ == '__main__':
    for i in range(-90, 90):
        print(converter(i, -32, -90, 90))
