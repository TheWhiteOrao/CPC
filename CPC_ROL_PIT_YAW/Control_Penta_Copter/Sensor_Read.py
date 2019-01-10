

# Sensor read, reads the sensors parameters and returns them as a tuple: [0] = accelerometer data, [1] = gyroscope data, [3] = temperature of the sensor.
# Sensors that can be used are mup9250 and lsm9ds1.
# output: {"acce": {"ax": i, "ay": i, "az": i}, "gyro": {"gx": i, "gy": i, "gz": i}}

def sensor_read(sensor):

    sensor_output = {}

    sensor.read_acc()
    sensor.read_gyro()
    sensor.read_temp()

    sensor_output["acce"]["ax"] = sensor.accelerometer_data[0]
    sensor_output["acce"]["ay"] = sensor.accelerometer_data[1]
    sensor_output["acce"]["az"] = sensor.accelerometer_data[2]

    sensor_output["gyro"]["gx"] = sensor.gyroscope_data[0]
    sensor_output["gyro"]["gy"] = sensor.gyroscope_data[1]
    sensor_output["gyro"]["gz"] = sensor.gyroscope_data[2]

    sensor_output["temp"] = sensor.temperature

    print(sensor_output)

    return sensor.accelerometer_data, sensor.gyroscope_data, sensor.temperature


if __name__ == '__main__':

    from N2.mpu9250 import *

    mpu9250 = MPU9250()
    mpu9250.initialize()

    print(sensor_read(mpu9250))
