

# Sensor read, reads the sensors parameters and returns them as a tuple: [0] = accelerometer data, [1] = gyroscope data, [3] = temperature of the sensor.
# Sensors that can be used are mup9250 and lsm9ds1.

def sensor_read(sensor):

    sensor.read_acc()
    sensor.read_gyro()
    sensor.read_temp()

    return sensor.accelerometer_data, sensor.gyroscope_data, sensor.temperature


if __name__ == '__main__':
    from N2.mpu9250 import *

    mpu9250 = MPU9250()

    mpu9250.initialize()

    print(sensor_read(mpu9250))
