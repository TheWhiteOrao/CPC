
Quaternion = {"QuaternionW": 1, "QuaternionX": 0, "QuaternionY": 0, "QuaternionZ": 0}
eInt = {"x": 0, "y": 0, "z": 0}


def inertial_measurement_unit(sensor_data, gyroscope_offset, Quaternion):

    # Normalise accelerometer measurement
    norm = (sensor_data["acce"]["ax"] * sensor_data["acce"]["ax"] + sensor_data["acce"]["ay"] * sensor_data["acce"]["ay"] + sensor_data["acce"]["az"] * sensor_data["acce"]["az"]) ** 0.5
    norm = 1 / norm  # use reciprocal for division
    sensor_data["acce"]["ax"] *= norm
    sensor_data["acce"]["ay"] *= norm
    sensor_data["acce"]["az"] *= norm

    # Estimated direction of gravity
    vx = 2 * (Quaternion["QuaternionX"] * Quaternion["QuaternionZ"] - Quaternion["QuaternionW"] * Quaternion["QuaternionY"])
    vy = 2 * (Quaternion["QuaternionW"] * Quaternion["QuaternionX"] + Quaternion["QuaternionY"] * Quaternion["QuaternionZ"])
    vz = Quaternion["QuaternionW"] * Quaternion["QuaternionW"] - Quaternion["QuaternionX"] * Quaternion["QuaternionX"] - Quaternion["QuaternionY"] * Quaternion["QuaternionY"] + Quaternion["QuaternionZ"] * Quaternion["QuaternionZ"]

    # Error is cross product between estimated direction and measured direction of gravity
    ex = (sensor_data["acce"]["ay"] * vz - sensor_data["acce"]["az"] * vy)
    ey = (sensor_data["acce"]["az"] * vx - sensor_data["acce"]["ax"] * vz)
    ez = (sensor_data["acce"]["ax"] * vy - sensor_data["acce"]["ay"] * vx)
    if Ki > 0:
        eInt[0] += ex  # accumulate integral error
        eInt[1] += ey
        eInt[2] += ez
    else:
        eInt[0] = 0  # prevent integral wind up
        eInt[1] = 0
        eInt[2] = 0

    # Apply feedback terms
    sensor_data["gyro"]["gx"] = sensor_data["gyro"]["gx"] + Kp * ex + Ki * eInt[0]
    sensor_data["gyro"]["gy"] = sensor_data["gyro"]["gy"] + Kp * ey + Ki * eInt[1]
    gz = gz + Kp * ez + Ki * eInt[2]

    # Integrate rate of change of quaternion
    pa = Quaternion["QuaternionX"]
    pb = Quaternion["QuaternionY"]
    pc = Quaternion["QuaternionZ"]
    Quaternion["QuaternionW"] = Quaternion["QuaternionW"] + (-Quaternion["QuaternionX"] * sensor_data["gyro"]["gx"] - Quaternion["QuaternionY"] * sensor_data["gyro"]["gy"] - Quaternion["QuaternionZ"] * gz) * (0.5 * SamplePeriod)
    Quaternion["QuaternionX"] = pa + (Quaternion["QuaternionW"] * sensor_data["gyro"]["gx"] + pb * gz - pc * sensor_data["gyro"]["gy"]) * (0.5 * SamplePeriod)
    Quaternion["QuaternionY"] = pb + (Quaternion["QuaternionW"] * sensor_data["gyro"]["gy"] - pa * gz + pc * sensor_data["gyro"]["gx"]) * (0.5 * SamplePeriod)
    Quaternion["QuaternionZ"] = pc + (Quaternion["QuaternionW"] * gz + pa * sensor_data["gyro"]["gy"] - pb * sensor_data["gyro"]["gx"]) * (0.5 * SamplePeriod)

    # Normalise quaternion
    norm = (Quaternion["QuaternionW"] * Quaternion["QuaternionW"] + Quaternion["QuaternionX"] * Quaternion["QuaternionX"] + Quaternion["QuaternionY"] * Quaternion["QuaternionY"] + Quaternion["QuaternionZ"] * Quaternion["QuaternionZ"]) ** 0.5
    norm = 1 / norm

    Quaternion["QuaternionW"] = Quaternion["QuaternionW"] * norm
    Quaternion["QuaternionX"] = Quaternion["QuaternionX"] * norm
    Quaternion["QuaternionY"] = Quaternion["QuaternionY"] * norm
    Quaternion["QuaternionZ"] = Quaternion["QuaternionZ"] * norm

    return Quaternion

    # print("ax: %-26s" % sensor_data["acce"]["ax"],
    #       "ay: %-26s" % sensor_data["acce"]["ay"],
    #       "az: %-26s" % sensor_data["acce"]["az"],
    #       "gx: %-26s" % sensor_data["gyro"]["gx"],
    #       "gy: %-26s" % sensor_data["gyro"]["gy"],
    #       "gz: %-26s" % sensor_data["gyro"]["gz"],
    #       "te: %-26s" % sensor_data["temp"])


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read

    sensor = sensor_initialize("mpu9250")

    while True:
        IMU = inertial_measurement_unit(sensor_read(sensor))
