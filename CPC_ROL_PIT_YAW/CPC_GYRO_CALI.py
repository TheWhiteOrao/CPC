from CPC_SENSORS_READ import sensor_read
from CPC_UNSLEEP import usleep

PI = 3.14159265358


def gyroscope_calibration(sensor, n=100):
    gyr_offset = [0, 0, 0]

    for i in range(n):
        acc_sen, gyr_sen, mag_sen, tem_sen = sensor_read(sensor)

        print(acc_sen, gyr_sen, mag_sen, tem_sen)

        gyr_x = gyr_sen[0]
        gyr_y = gyr_sen[1]
        gyr_z = gyr_sen[2]

        gyr_x *= 180 / PI
        gyr_y *= 180 / PI
        gyr_z *= 180 / PI

        gyr_offset[0] += (-gyr_x * 0.0175) / n
        gyr_offset[1] += (-gyr_y * 0.0175) / n
        gyr_offset[2] += (-gyr_z * 0.0175) / n
        usleep(10000)

    return gyr_offset
