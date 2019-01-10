
# imput: sensor read MPU9250 accelerometer_data, gyroscope_data
# output: roll and pitch not converted in a dictionary. like this {roll:deg, pitch:deg}


def inertiale_messeinheit(sensor_data):
    pass


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read

    sensor = sensor_initialize("mpu9250")
    sensor_data = sensor_read(sensor)
    print(sensor_data)
