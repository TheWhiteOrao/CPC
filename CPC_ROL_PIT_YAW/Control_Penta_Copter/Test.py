
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

# x = 5
# y = 6
# z = 7
#
# norm = 1 / (x**2 + y**2 + z**2)**0.5
#
# print((x * norm)**2 + (y * norm)**2 + (z * norm)**2)


# Quaternion

# Quaternion = (QuaternionR, QuaternionI, QuaternionJ, QuaternionK)
# Quaternion = Quaternion + Quaternion * I + Quaternion * J + Quaternion * K
# public void Update(float gx, float gy, float gz, float ax, float ay, float az, float mx, float my, float mz)
# {
#     float q1 = Quaternion[0], q2 = Quaternion[1], q3 = Quaternion[2], q4 = Quaternion[3]
#     // short name local variable for readability
#     float norm
#     float hx, hy, bx, bz
#     float vx, vy, vz, wx, wy, wz
#     float ex, ey, ez
#     float pa, pb, pc
#
#     // Auxiliary variables to avoid repeated arithmetic
#     float q1q1 = q1 * q1
#     float q1q2 = q1 * q2
#     float q1q3 = q1 * q3
#     float q1q4 = q1 * q4
#     float q2q2 = q2 * q2
#     float q2q3 = q2 * q3
#     float q2q4 = q2 * q4
#     float q3q3 = q3 * q3
#     float q3q4 = q3 * q4
#     float q4q4 = q4 * q4
#
#     // Normalise accelerometer measurement
#     norm = (float)Math.Sqrt(ax * ax + ay * ay + az * az)
#     if (norm == 0f) return
#     // handle NaN
#     norm = 1 / norm
#     // use reciprocal for division
#     ax *= norm
#     ay *= norm
#     az *= norm
#
#     // Normalise magnetometer measurement
#     norm = (float)Math.Sqrt(mx * mx + my * my + mz * mz)
#     if (norm == 0f) return
#     // handle NaN
#     norm = 1 / norm
#     // use reciprocal for division
#     mx *= norm
#     my *= norm
#     mz *= norm
#
#     // Reference direction of Earth's magnetic field
#     hx = 2f * mx * (0.5f - q3q3 - q4q4) + 2f * my * (q2q3 - q1q4) + 2f * mz * (q2q4 + q1q3)
#     hy = 2f * mx * (q2q3 + q1q4) + 2f * my * (0.5f - q2q2 - q4q4) + 2f * mz * (q3q4 - q1q2)
#     bx = (float)Math.Sqrt((hx * hx) + (hy * hy))
#     bz = 2f * mx * (q2q4 - q1q3) + 2f * my * (q3q4 + q1q2) + 2f * mz * (0.5f - q2q2 - q3q3)
#
#     // Estimated direction of gravity and magnetic field
#     vx = 2f * (q2q4 - q1q3)
#     vy = 2f * (q1q2 + q3q4)
#     vz = q1q1 - q2q2 - q3q3 + q4q4
#     wx = 2f * bx * (0.5f - q3q3 - q4q4) + 2f * bz * (q2q4 - q1q3)
#     wy = 2f * bx * (q2q3 - q1q4) + 2f * bz * (q1q2 + q3q4)
#     wz = 2f * bx * (q1q3 + q2q4) + 2f * bz * (0.5f - q2q2 - q3q3)
#
#     // Error is cross product between estimated direction and measured direction of gravity
#     ex = (ay * vz - az * vy) + (my * wz - mz * wy)
#     ey = (az * vx - ax * vz) + (mz * wx - mx * wz)
#     ez = (ax * vy - ay * vx) + (mx * wy - my * wx)
#     if (Ki > 0f)
#     {
#         eInt[0] += ex
#         // accumulate integral error
#         eInt[1] += ey
#         eInt[2] += ez
#     }
#     else
#     {
#         eInt[0] = 0.0f
#         // prevent integral wind up
#         eInt[1] = 0.0f
#         eInt[2] = 0.0f
#     }
#
#     // Apply feedback terms
#     gx = gx + Kp * ex + Ki * eInt[0]
#     gy = gy + Kp * ey + Ki * eInt[1]
#     gz = gz + Kp * ez + Ki * eInt[2]
#
#     // Integrate rate of change of quaternion
#     pa = q2
#     pb = q3
#     pc = q4
#     q1 = q1 + (-q2 * gx - q3 * gy - q4 * gz) * (0.5f * SamplePeriod)
#     q2 = pa + (q1 * gx + pb * gz - pc * gy) * (0.5f * SamplePeriod)
#     q3 = pb + (q1 * gy - pa * gz + pc * gx) * (0.5f * SamplePeriod)
#     q4 = pc + (q1 * gz + pa * gy - pb * gx) * (0.5f * SamplePeriod)
#
#     // Normalise quaternion
#     norm = (float)Math.Sqrt(q1 * q1 + q2 * q2 + q3 * q3 + q4 * q4)
#     norm = 1.0f / norm
#     Quaternion[0] = q1 * norm
#     Quaternion[1] = q2 * norm
#     Quaternion[2] = q3 * norm
#     Quaternion[3] = q4 * norm
# }

# from time import perf_counter_ns
#
# g = perf_counter_ns()
# for i in range(10000):
#     h = perf_counter_ns()
#     print(1000000000 / (h - g))
#     g = h

x, y, z = 0, 1, 2


def g():
    global x, y, z
    x += 3
    y += 2
    z += 1
    return x, y, z


print(g())
