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

def converter(imp, imp_kor, min=-180, max=180):
    lol = max - imp_kor
    lolo = min - imp_kor
    #print(lol, lolo)

    l = max - imp_kor
    k = min - imp_kor
    g = max - imp
    j = min - imp
    o = (l - k) - g
    p = (l - k) - j
    if imp_kor > 0:
        if imp < lolo:
            return((o + l) - lol - lolo)
        else:
            return((o + k) - lol - lolo)
    else:
        if imp < lol:
            return((o + l) - lol * 2)
        else:
            return((o + k) - lol * 2)


for i in range(-180, 180):
    print(i, converter(i, -10))
