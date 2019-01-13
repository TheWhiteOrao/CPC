

def inertial_measurement_unit(sensor_data, gyroscope_offset, delta_time, Quaternion={"QuaternionR": 1, "QuaternionI": 0, "QuaternionJ": 0, "QuaternionK": 0}, eInt={"I": 0, "J": 0, "K": 0}, Kp=2, Ki=0):

    # -------------------- Auxiliary variables to avoid repeated arithmetic ------------------- #

    QuaternionRR = Quaternion["QuaternionR"] * Quaternion["QuaternionR"]
    QuaternionRI = Quaternion["QuaternionR"] * Quaternion["QuaternionI"]
    QuaternionRJ = Quaternion["QuaternionR"] * Quaternion["QuaternionJ"]
    QuaternionRK = Quaternion["QuaternionR"] * Quaternion["QuaternionK"]
    QuaternionII = Quaternion["QuaternionI"] * Quaternion["QuaternionI"]
    QuaternionIJ = Quaternion["QuaternionI"] * Quaternion["QuaternionJ"]
    QuaternionIK = Quaternion["QuaternionI"] * Quaternion["QuaternionK"]
    QuaternionJJ = Quaternion["QuaternionJ"] * Quaternion["QuaternionJ"]
    QuaternionJK = Quaternion["QuaternionJ"] * Quaternion["QuaternionK"]
    QuaternionKK = Quaternion["QuaternionK"] * Quaternion["QuaternionK"]

    # ------------------------------------------------------------------------------------------ #
    # -------------------------- Normalise accelerometer measurement --------------------------- #
    acceNorm = (
        sensor_data["acce"]["ax"] ** 2 +
        sensor_data["acce"]["ay"] ** 2 +
        sensor_data["acce"]["az"] ** 2) ** 0.5

    sensor_data["acce"]["ax"] /= acceNorm
    sensor_data["acce"]["ay"] /= acceNorm
    sensor_data["acce"]["az"] /= acceNorm

    # print(round(
    #     sensor_data["acce"]["ax"]**2 +
    #     sensor_data["acce"]["ay"]**2 +
    #     sensor_data["acce"]["az"]**2, 15)
    # )

    # ------------------------------------------------------------------------------------------ #
    # --------------------------- Normalise magnetometer measurement --------------------------- #
    #
    magnNorm = (
        sensor_data["magn"]["mx"] ** 2 +
        sensor_data["magn"]["my"] ** 2 +
        sensor_data["magn"]["mz"] ** 2) ** 0.5

    sensor_data["magn"]["mx"] /= magnNorm
    sensor_data["magn"]["my"] /= magnNorm
    sensor_data["magn"]["mz"] /= magnNorm

    # print(round(
    #     sensor_data["magn"]["mx"]**2 +
    #     sensor_data["magn"]["my"]**2 +
    #     sensor_data["magn"]["mz"]**2, 15)
    # )

    # ------------------------------------------------------------------------------------------ #
    # ------------------------------------ Gyroscope offset ------------------------------------ #

    sensor_data["gyro"]["gx"] -= gyroscope_offset["gx"]
    sensor_data["gyro"]["gy"] -= gyroscope_offset["gy"]
    sensor_data["gyro"]["gz"] -= gyroscope_offset["gz"]

    # ------------------------------------------------------------------------------------------ #
    # --------------------- Reference direction of Earth's magnetic field  --------------------- #
    #
    hx = 2 * sensor_data["magn"]["mx"] * (0.5 - QuaternionJJ - QuaternionKK) + 2 * sensor_data["magn"]["my"] * (QuaternionIJ - QuaternionRK) + 2 * sensor_data["magn"]["mz"] * (QuaternionIK + QuaternionRJ)
    hy = 2 * sensor_data["magn"]["mx"] * (QuaternionIJ + QuaternionRK) + 2 * sensor_data["magn"]["my"] * (0.5 - QuaternionII - QuaternionKK) + 2 * sensor_data["magn"]["mz"] * (QuaternionJK - QuaternionRI)
    bx = ((hx * hx) + (hy * hy)) ** 0.5
    bz = 2 * sensor_data["magn"]["mx"] * (QuaternionIK - QuaternionRJ) + 2 * sensor_data["magn"]["my"] * (QuaternionJK + QuaternionRI) + 2 * sensor_data["magn"]["mz"] * (0.5 - QuaternionII - QuaternionJJ)

    # ------------------------------------------------------------------------------------------ #
    # -------------------- Estimated direction of gravity and magnetic field ------------------- #

    # ---------------------------------- Gravity direction ------------------------------------- #
    vx = 2 * (QuaternionIK - QuaternionRJ)
    vy = 2 * (QuaternionRI + QuaternionJK)
    vz = QuaternionRR - QuaternionII - QuaternionJJ + QuaternionKK

    # ------------------------------------ Magnetic field -------------------------------------- #
    wx = 2 * bx * (0.5 - QuaternionJJ - QuaternionKK) + 2 * bz * (QuaternionIK - QuaternionRJ)
    wy = 2 * bx * (QuaternionIJ - QuaternionRK) + 2 * bz * (QuaternionRI + QuaternionJK)
    wz = 2 * bx * (QuaternionRJ + QuaternionIK) + 2 * bz * (0.5 - QuaternionII - QuaternionJJ)

    # ------------------------------------------------------------------------------------------ #
    # -- Error is cross product between estimated direction and measured direction of gravity -- #

    # ---------------------------------- Gravity direction ------------------------------------- #
    # ex = (sensor_data["acce"]["ay"] * vz - sensor_data["acce"]["az"] * vy)
    # ey = (sensor_data["acce"]["az"] * vx - sensor_data["acce"]["ax"] * vz)
    # ez = (sensor_data["acce"]["ax"] * vy - sensor_data["acce"]["ay"] * vx)
    # ------------------------------------ Magnetic field -------------------------------------- #
    ex = (sensor_data["acce"]["ay"] * vz - sensor_data["acce"]["az"] * vy) + (sensor_data["magn"]["my"] * wz - sensor_data["magn"]["mz"] * wy)
    ey = (sensor_data["acce"]["az"] * vx - sensor_data["acce"]["ax"] * vz) + (sensor_data["magn"]["mz"] * wx - sensor_data["magn"]["mx"] * wz)
    ez = (sensor_data["acce"]["ax"] * vy - sensor_data["acce"]["ay"] * vx) + (sensor_data["magn"]["mx"] * wy - sensor_data["magn"]["my"] * wx)

    if Ki > 0:

        # accumulate integral error
        eInt["I"] += ex
        eInt["J"] += ey
        eInt["K"] += ez

    else:

        # prevent integral wind up
        eInt["I"] = 0.0
        eInt["J"] = 0.0
        eInt["K"] = 0.0

    # ------------------------------------------------------------------------------------------ #
    # ---------------------------------- Apply feedback terms ---------------------------------- #

    sensor_data["gyro"]["gx"] = sensor_data["gyro"]["gx"] + Kp * ex + Ki * eInt["I"]
    sensor_data["gyro"]["gy"] = sensor_data["gyro"]["gy"] + Kp * ey + Ki * eInt["J"]
    sensor_data["gyro"]["gz"] = sensor_data["gyro"]["gz"] + Kp * ez + Ki * eInt["K"]

    # ------------------------------------------------------------------------------------------ #
    # ------------------------- Integrate rate of change of quaternion ------------------------- #

    pa = Quaternion["QuaternionI"]
    pb = Quaternion["QuaternionJ"]
    pc = Quaternion["QuaternionK"]
    Quaternion["QuaternionR"] = Quaternion["QuaternionR"] + (-Quaternion["QuaternionI"] * sensor_data["gyro"]["gx"] - Quaternion["QuaternionJ"] * sensor_data["gyro"]["gy"] - Quaternion["QuaternionK"] * sensor_data["gyro"]["gz"]) * (0.5 * delta_time)
    Quaternion["QuaternionI"] = pa + (Quaternion["QuaternionR"] * sensor_data["gyro"]["gx"] + pb * sensor_data["gyro"]["gz"] - pc * sensor_data["gyro"]["gy"]) * (0.5 * delta_time)
    Quaternion["QuaternionJ"] = pb + (Quaternion["QuaternionR"] * sensor_data["gyro"]["gy"] - pa * sensor_data["gyro"]["gz"] + pc * sensor_data["gyro"]["gx"]) * (0.5 * delta_time)
    Quaternion["QuaternionK"] = pc + (Quaternion["QuaternionR"] * sensor_data["gyro"]["gz"] + pa * sensor_data["gyro"]["gy"] - pb * sensor_data["gyro"]["gx"]) * (0.5 * delta_time)

    # ------------------------------------------------------------------------------------------ #
    # ---------------------------------- Normalise quaternion ---------------------------------- #

    normQuat = (
        Quaternion["QuaternionR"] ** 2 +
        Quaternion["QuaternionI"] ** 2 +
        Quaternion["QuaternionJ"] ** 2 +
        Quaternion["QuaternionK"] ** 2) ** 0.5

    Quaternion["QuaternionR"] = Quaternion["QuaternionR"] / normQuat
    Quaternion["QuaternionI"] = Quaternion["QuaternionI"] / normQuat
    Quaternion["QuaternionJ"] = Quaternion["QuaternionJ"] / normQuat
    Quaternion["QuaternionK"] = Quaternion["QuaternionK"] / normQuat

    # ------------------------------------------------------------------------------------------ #
    # print("ax: %-26s" % sensor_data["acce"]["ax"],
    #       "ay: %-26s" % sensor_data["acce"]["ay"],
    #       "az: %-26s" % sensor_data["acce"]["az"],
    #       "gx: %-26s" % sensor_data["gyro"]["gx"],
    #       "gy: %-26s" % sensor_data["gyro"]["gy"],
    #       "gz: %-26s" % sensor_data["gyro"]["gz"],
    #       "te: %-26s" % sensor_data["temp"])

    return Quaternion


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read
    from Gyrometer_Calibration import gyroscope_calibration
    from Delta_Time import calculate_delta_time
    from Euler_Angle import euler_angle
    from math import acos, pi

    sensor = sensor_initialize("lsm9ds1")

    gyroscope_offset = gyroscope_calibration(sensor)

    delta_time, Hz, current_delta_time = calculate_delta_time()

    Quaternion = inertial_measurement_unit(sensor_read(sensor), gyroscope_offset, delta_time)

    while True:

        delta_time, Hz, current_delta_time = calculate_delta_time(current_delta_time, Hz)

        Quaternion = inertial_measurement_unit(sensor_read(sensor), gyroscope_offset, delta_time, Quaternion)
        print("QuaternionR: %-26s" % ((acos(Quaternion["QuaternionR"]) * 2) * 90 / pi),
              "QuaternionI: %-26s" % ((acos(Quaternion["QuaternionI"]) * 2) * 90 / pi),
              "QuaternionJ: %-26s" % ((acos(Quaternion["QuaternionJ"]) * 2) * 90 / pi),
              "QuaternionK: %-26s" % ((acos(Quaternion["QuaternionK"]) * 2) * 90 / pi))

#  quat [-0.3832534449239102, -0.00516282644230581, 0.014133308871725835, 0.9235206504228362] RATE 599
#
# {'0.2914464432719522,  0.04652607218289297,  -0.004588636499230154,  0.9554440013556205}
