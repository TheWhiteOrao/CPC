
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

# from Receiver_Input import receiver_imput
# from Receiver_Signal_Converter import receiver_signal_converter
# from time import process_time_ns
#
# h = 0
# while True:
#     # receiver_signal_converter(receiver_imput({0: (0, 1), 1: (-1, 1), 2: (-1, 1), 3: (-1, 1)}))
#     print(1000000000 / (process_time_ns() - h))
#     h = process_time_ns()

#
# h = {1: 0}
#
# if h == dict():
#     print("emty")
# elif type(h) == dict:
#     print("full")
# else:
#     print("rong type")
#!/usr/bin/python
#	This is the base code needed to get usable angles from a BerryIMU
#	using a Complementary filter. The readings can be improved by
#	adding more filters, E.g Kalman, Low pass, median filter, etc..
#   See berryIMU.py for more advanced code.
#
#	For this code to work correctly, BerryIMU must be facing the
#	correct way up. This is when the Skull Logo on the PCB is facing down.
#
#   Both the BerryIMUv1 and BerryIMUv2 are supported
#
#	http://ozzmaker.com/
# # Gyroscope offset
# sensor_data["gyro"]["gx"] -= gyroscope_offset["gx"]
# sensor_data["gyro"]["gy"] -= gyroscope_offset["gy"]
# sensor_data["gyro"]["gz"] -= gyroscope_offset["gz"]
#
# # Normalise accelerometer measurement
# norm = (sensor_data["acce"]["ax"] * sensor_data["acce"]["ax"] + sensor_data["acce"]["ay"] * sensor_data["acce"]["ay"] + sensor_data["acce"]["az"] * sensor_data["acce"]["az"]) ** 0.5
# norm = 1 / norm  # use reciprocal for division
# sensor_data["acce"]["ax"] *= norm
# sensor_data["acce"]["ay"] *= norm
# sensor_data["acce"]["az"] *= norm
#
# # Estimated direction of gravity
# vx = 2 * (Quaternion["QuaternionX"] * Quaternion["QuaternionZ"] - Quaternion["QuaternionW"] * Quaternion["QuaternionY"])
# vy = 2 * (Quaternion["QuaternionW"] * Quaternion["QuaternionX"] + Quaternion["QuaternionY"] * Quaternion["QuaternionZ"])
# vz = Quaternion["QuaternionW"] * Quaternion["QuaternionW"] - Quaternion["QuaternionX"] * Quaternion["QuaternionX"] - Quaternion["QuaternionY"] * Quaternion["QuaternionY"] + Quaternion["QuaternionZ"] * Quaternion["QuaternionZ"]
#
# # Error is cross product between estimated direction and measured direction of gravity
# ex = (sensor_data["acce"]["ay"] * vz - sensor_data["acce"]["az"] * vy)
# ey = (sensor_data["acce"]["az"] * vx - sensor_data["acce"]["ax"] * vz)
# ez = (sensor_data["acce"]["ax"] * vy - sensor_data["acce"]["ay"] * vx)
# if Ki > 0:
#     eInt["x"] += ex  # accumulate integral error
#     eInt["y"] += ey
#     eInt["z"] += ez
# else:
#     eInt["x"] = 0  # prevent integral wind up
#     eInt["y"] = 0
#     eInt["z"] = 0
#
# # Apply feedback terms
# sensor_data["gyro"]["gx"] = sensor_data["gyro"]["gx"] + Kp * ex + Ki * eInt["x"]
# sensor_data["gyro"]["gy"] = sensor_data["gyro"]["gy"] + Kp * ey + Ki * eInt["y"]
# sensor_data["gyro"]["gz"] = sensor_data["gyro"]["gz"] + Kp * ez + Ki * eInt["z"]
#
# # Integrate rate of change of quaternion
# pa = Quaternion["QuaternionX"]
# pb = Quaternion["QuaternionY"]
# pc = Quaternion["QuaternionZ"]
# Quaternion["QuaternionW"] = Quaternion["QuaternionW"] + (-Quaternion["QuaternionX"] * sensor_data["gyro"]["gx"] - Quaternion["QuaternionY"] * sensor_data["gyro"]
#                                                          ["gy"] - Quaternion["QuaternionZ"] * sensor_data["gyro"]["gz"]) * (0.5 * delta_time)
# Quaternion["QuaternionX"] = pa + (Quaternion["QuaternionW"] * sensor_data["gyro"]["gx"] + pb * sensor_data["gyro"]["gz"] - pc * sensor_data["gyro"]["gy"]) * (0.5 * delta_time)
# Quaternion["QuaternionY"] = pb + (Quaternion["QuaternionW"] * sensor_data["gyro"]["gy"] - pa * sensor_data["gyro"]["gz"] + pc * sensor_data["gyro"]["gx"]) * (0.5 * delta_time)
# Quaternion["QuaternionZ"] = pc + (Quaternion["QuaternionW"] * sensor_data["gyro"]["gz"] + pa * sensor_data["gyro"]["gy"] - pb * sensor_data["gyro"]["gx"]) * (0.5 * delta_time)
#
# # Normalise quaternion
# norm = (Quaternion["QuaternionW"] * Quaternion["QuaternionW"] + Quaternion["QuaternionX"] * Quaternion["QuaternionX"] + Quaternion["QuaternionY"] * Quaternion["QuaternionY"] + Quaternion["QuaternionZ"] * Quaternion["QuaternionZ"]) ** 0.5
# norm = 1 / norm
#
# Quaternion["QuaternionW"] = Quaternion["QuaternionW"] * norm
# Quaternion["QuaternionX"] = Quaternion["QuaternionX"] * norm
# Quaternion["QuaternionY"] = Quaternion["QuaternionY"] * norm
# Quaternion["QuaternionZ"] = Quaternion["QuaternionZ"] * norm
