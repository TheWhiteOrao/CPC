
def lsm9ds1_sensor_read(lsm9ds1):
    lsm9ds1.read_acc()
    lsm9ds1.read_gyro()
    lsm9ds1.read_mag()
    lsm9ds1.read_temp()

    return lsm9ds1.accelerometer_data, lsm9ds1.gyroscope_data, lsm9ds1.magnetometer_data, lsm9ds1.temperature
