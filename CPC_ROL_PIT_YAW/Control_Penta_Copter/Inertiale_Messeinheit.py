
# imput: sensor read MPU9250 accelerometer_data, gyroscope_data
# output: roll and pitch not converted in a dictionary. like this {roll:deg, pitch:deg}


def inertiale_messeinheit(sensor_data):
    accelerometer_data, gyroscope_data, temperature = sensor_data
    accelerometer_data accelerometer_data

    print("acce: %-26s" % accelerometer_data,
          "gyro: %-26s" % gyroscope_data,
          "temp: %-26s" % temperature)


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read

    sensor = sensor_initialize("mpu9250")

    for i in range(1000):
        IMU = inertiale_messeinheit(sensor_read(sensor))
