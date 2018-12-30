from CPC_NAVIO2.lsm9ds1 import *
from CPC_NAVIO2.mpu9250 import *

lsm9ds1 = LSM9DS1()
mpu9250 = MPU9250()

lsm9ds1.initialize()
mpu9250.initialize()

while True:

lsm = lsm9ds1.getMotion9()
mpu = mpu9250.getMotion9()

print(lsm, mpu)
