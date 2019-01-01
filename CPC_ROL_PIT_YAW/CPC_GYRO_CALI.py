from CPC_SENSORS_READ import sensor_read


def gyroscope_calibration(sensor, n=100):
    for i in range(n)
        acc_sen, gyr_sen, mag_sen, tem_sen = sensor_read(sensor)
