from Sensor_Read import sensor_read
from Micro_Sleep import micro_sleep

PI = 3.14159265358


def gyroscope_calibration(sensor_type, interval=100):

    gyroscope_offset = [0, 0, 0]

    for i in range(interval):

        sensor_data = sensor_read(sensor_type)

        gyroscopeX = sensor_data["gyro"]["gx"]
        gyroscopeY = sensor_data["gyro"]["gy"]
        gyroscopeZ = sensor_data["gyro"]["gz"]

        gyroscopeX *= 180 / PI
        gyroscopeY *= 180 / PI
        gyroscopeZ *= 180 / PI

        gyroscope_offset[0] += (-gyroscopeX * 0.0175) / interval
        gyroscope_offset[1] += (-gyroscopeY * 0.0175) / interval
        gyroscope_offset[2] += (-gyroscopeZ * 0.0175) / interval

        micro_sleep(10000)

    return gyroscope_offset


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize

    print(gyroscope_calibration(sensor_initialize("mpu9250")))
