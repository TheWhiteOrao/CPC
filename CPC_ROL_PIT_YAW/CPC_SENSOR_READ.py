from time import *
from CPC_NA2.mpu9250 import *
from CPC_NA2.lsm9ds1 import *
from CPC_MPU9250_READ import mpu9250_sensor_read
from CPC_LSM9DS1_READ import lsm9ds1_sensor_read

mpu9250 = MPU9250()
lsm9ds1 = LSM9DS1()

mpu9250.initialize()
lsm9ds1.initialize()

while True:
    print(mpu9250_sensor_read(mpu9250))
    print(lsm9ds1_sensor_read(lsm9ds1))
