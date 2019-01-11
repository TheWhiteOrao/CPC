

def inertial_measurement_unit(sensor_data):

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
