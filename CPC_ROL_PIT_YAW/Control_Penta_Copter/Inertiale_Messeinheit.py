
# imput: sensor read MPU9250 accelerometer_data, gyroscope_data
# output: roll and pitch not converted in a dictionary. like this {roll:deg, pitch:deg}


def inertiale_messeinheit(sensor_data):
    sensor_dict = sensor_data

    print("ax: %-26s" % sensor_dict["acce"]["ax"],
          "ay: %-26s" % sensor_dict["acce"]["ay"],
          "az: %-26s" % sensor_dict["acce"]["az"],
          "gx: %-26s" % sensor_dict["gyro"]["gx"],
          "gy: %-26s" % sensor_dict["gyro"]["gy"],
          "gz: %-26s" % sensor_dict["gyro"]["gz"],
          "te: %-26s" % sensor_dict["temp"])


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read

    sensor = sensor_initialize("mpu9250")

    for i in range(1000):
        IMU = inertiale_messeinheit(sensor_read(sensor))
