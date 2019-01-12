

def inertial_measurement_unit(sensor_data, gyroscope_offset, delta_time, Quaternion={"QuaternionW": 1, "QuaternionX": 0, "QuaternionY": 0, "QuaternionZ": 0}, Kp):

    print("ax: %-26s" % sensor_data["acce"]["ax"],
          "ay: %-26s" % sensor_data["acce"]["ay"],
          "az: %-26s" % sensor_data["acce"]["az"],
          "gx: %-26s" % sensor_data["gyro"]["gx"],
          "gy: %-26s" % sensor_data["gyro"]["gy"],
          "gz: %-26s" % sensor_data["gyro"]["gz"],
          "te: %-26s" % sensor_data["temp"])

    return Quaternion


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read
    from Gyrometer_Calibration import gyroscope_calibration
    from Delta_Time import calculate_delta_time
    from Euler_Angle import euler_angle

    sensor = sensor_initialize("mpu9250")

    gyroscope_offset = gyroscope_calibration(sensor)

    delta_time, Hz, current_delta_time = calculate_delta_time()

    Quaternion = inertial_measurement_unit(sensor_read(sensor), gyroscope_offset, delta_time)

    while True:

        delta_time, Hz, current_delta_time = calculate_delta_time(current_delta_time, Hz)

        Quaternion, eInt = inertial_measurement_unit(sensor_read(sensor), gyroscope_offset, delta_time, Quaternion)
        print(euler_angle(Quaternion), Hz)
