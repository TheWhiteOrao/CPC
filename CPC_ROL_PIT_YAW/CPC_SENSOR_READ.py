from time import *
from CPC_NA2.mpu9250 import *
from CPC_NA2.lsm9ds1 import *
from test import *

mpu9250 = MPU9250()
lsm9ds1 = LSM9DS1()

mpu9250.initialize()
lsm9ds1.initialize()

print(test())
