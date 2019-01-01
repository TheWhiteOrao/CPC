
def mpu9250_sensor_read(mpu9250):
    mpu9250.read_acc()
    mpu9250.read_gyro()
    mpu9250.read_mag()
    mpu9250.read_temp()

    return mpu9250.accelerometer_data, mpu9250.gyroscope_data, mpu9250.magnetometer_data, mpu9250.temperature
