
# imput: sensor read MPU9250 accelerometer_data, gyroscope_data
# output: roll and pitch not converted in a dictionary. like this {roll:deg, pitch:deg}


def inertiale_messeinheit(sensor_data, hz):
    sensor_dict = sensor_data

    print("ax: %-26s" % sensor_dict["acce"]["ax"],
          "ay: %-26s" % sensor_dict["acce"]["ay"],
          "az: %-26s" % sensor_dict["acce"]["az"],
          "gx: %-26s" % sensor_dict["gyro"]["gx"],
          "gy: %-26s" % sensor_dict["gyro"]["gy"],
          "gz: %-26s" % sensor_dict["gyro"]["gz"],
          "te: %-26s" % sensor_dict["temp"],
          "hz: %-26s" % hz)


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read
    from time import process_time_ns

    ns = 0

    sensor = sensor_initialize("mpu9250")

    while True:
        IMU = inertiale_messeinheit(sensor_read(sensor), hz)

        hz = (1000000000 / (process_time_ns() - ns))
        ns = process_time_ns()
