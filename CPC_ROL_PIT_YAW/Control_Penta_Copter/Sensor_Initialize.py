

def sensor_initialize(sensor_name):

    if sensor_name == "mpu9250":

        from N2.mpu9250 import MPU9250
        sensor_of_choice = MPU9250()

    elif sensor_name == "lsm9ds1":

        from N2.lsm9ds1 import LSM9DS1
        sensor_of_choice = LSM9DS1()

    else:
        print("not an imported sensor")

    sensor_of_choice.initialize()

    return sensor_of_choice


if __name__ == '__main__':
    print(sensor_initialize("mpu9250"))
