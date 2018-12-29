from time import *

# while True:


def usleep(x):
    return sleep(x / 1000000.0)


currenttime = 0


def imuLoop():
    global currenttime
    previoustime = currenttime
    currenttime = time_ns()
    dt = (currenttime - previoustime) / 1000000000

    if dt < (1 / 1300):
        usleep((1 / 1300 - dt) * 1000000)
        currenttime = time_ns()

    dt = (currenttime - previoustime) / 1000000000

    print(dt, currenttime, previoustime)



# def usleep(x):
#     return sleep(x / 1000000.0)
i = 0
while i < 100:
    imuLoop()
    i += 1

# from CPC_CO import *
# rotor_radius = 500
# engine_force = 10000
#
# basic_lever = engine_force * rotor_radius
#
# # engine_one_x = 90
# engine_one_y = 0
#
# engine_two_x = 18
# engine_two_y = 72
#
# engine_thr_x = 54
# engine_thr_y = 36
#
# engine_fou_x = 54
# engine_fou_y = 36
#
# engine_fiv_x = 18
# engine_fiv_y = 72
#
# # engine_one_length_to_x = CO(engine_one_x) * rotor_radius
# engine_one_length_to_y = CO(engine_one_y) * rotor_radius
#
# engine_two_length_to_x = CO(engine_two_x) * rotor_radius
# engine_two_length_to_y = CO(engine_two_y) * rotor_radius
#
# engine_thr_length_to_x = CO(engine_thr_x) * rotor_radius
# engine_thr_length_to_y = CO(engine_thr_y) * rotor_radius
#
# engine_fou_length_to_x = CO(engine_fou_x) * rotor_radius
# engine_fou_length_to_y = CO(engine_fou_y) * rotor_radius
#
# engine_fiv_length_to_x = CO(engine_fiv_x) * rotor_radius
# engine_fiv_length_to_y = CO(engine_fiv_y) * rotor_radius
#
# # engine_one_lever_x = basic_lever / (engine_one_length_to_x * engine_force)
# engine_one_lever_y = basic_lever / (engine_one_length_to_y * engine_force)
#
# engine_two_lever_x = basic_lever / (engine_two_length_to_x * engine_force)
# engine_two_lever_y = basic_lever / (engine_two_length_to_y * engine_force)
#
# engine_thr_lever_x = basic_lever / (engine_thr_length_to_x * engine_force)
# engine_thr_lever_y = basic_lever / (engine_thr_length_to_y * engine_force)
#
# engine_fou_lever_x = basic_lever / (engine_fou_length_to_x * engine_force)
# engine_fou_lever_y = basic_lever / (engine_fou_length_to_y * engine_force)
#
# engine_fiv_lever_x = basic_lever / (engine_fiv_length_to_x * engine_force)
# engine_fiv_lever_y = basic_lever / (engine_fiv_length_to_y * engine_force)
#
#
# # f = engine_125
#
# engine_one_f = engine_one_lever_y / 3
# engine_two_f = engine_two_lever_y / 3
# engine_fiv_f = engine_fiv_lever_y / 3
#
# # r = engine_23
#
# engine_two_r = engine_two_lever_x / 2
# engine_thr_r = engine_thr_lever_x / 2
#
# # b = engine_34
#
# engine_thr_b = engine_thr_lever_y / 2
# engine_fou_b = engine_fou_lever_y / 2
#
# # l = engine 45
#
# engine_fou_l = engine_fou_lever_x / 2
# engine_fiv_l = engine_fiv_lever_x / 2
#
#
# print(0.84 * 0.25 * (engine_one_f * 0.25), "f")
# print(0.84 * 0.25 * (engine_two_f * 0.25), "f")
# print(0.84 * 0.25 * (engine_fiv_f * 0.25), "f \n")
#
# print(0.84 * 0.25 * (engine_two_r * 0.25), "r")
# print(0.84 * 0.25 * (engine_thr_r * 0.25), "r \n")
#
# print(0.84 * 0.25 * (engine_thr_b * 0.25), "b")
# print(0.84 * 0.25 * (engine_fou_b * 0.25), "b \n")
#
# print(0.84 * 0.25 * (engine_fou_l * 0.25), "l")
# print(0.84 * 0.25 * (engine_fiv_l * 0.25), "l \n")

# print("%-2s" % 1, "hii")
# print("%-2s" % -1, "hii")

#
# def im():
#     g = [1, 2, 3]
#     l = [4, 3, 5]
#
#     return g, l
#
#
# h[0], t[1], g[2], l = im()
#
# print(t, l)

# offset = [0, 0, 0]
#
# offset[0] += 1
# offset[1] += 2
# offset[2] += 3
#
# print(offset[0], offset[1], offset[2])
# print("Offsets are: {0} {1} {2}\n".format(offset[0], offset[1], offset[2]))
# usleep(10000)
