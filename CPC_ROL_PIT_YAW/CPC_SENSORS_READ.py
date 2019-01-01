
def sensor_read(sensor):
    sensor.read_acc()
    sensor.read_gyro()
    sensor.read_mag()
    sensor.read_temp()

    return sensor.accelerometer_data, sensor.gyroscope_data, sensor.magnetometer_data, sensor.temperature
