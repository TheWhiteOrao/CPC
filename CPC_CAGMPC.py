from CPC_NAVIO2.lsm9ds1 import *
from CPC_NAVIO2.mpu9250 import *

lsm9ds1 = LSM9DS1()
mpu9250 = MPU9250()

lsm9ds1.initialize()
mpu9250.initialize()

while True:

    lsm_agxyz = lsm9ds1.getMotion6()
    mpu_agxyz = mpu9250.getMotion6()

    lsm_ax = lsm_agxyz[0]
    lsm_ay = lsm_agxyz[1]
    lsm_az = lsm_agxyz[2]
    lsm_gx = lsm_agxyz[3]
    lsm_gy = lsm_agxyz[4]
    lsm_gz = lsm_agxyz[5]

    mpu_ax = mpu_agxyz[0]
    mpu_ay = mpu_agxyz[1]
    mpu_az = mpu_agxyz[2]
    mpu_gx = mpu_agxyz[3]
    mpu_gy = mpu_agxyz[4]
    mpu_gz = mpu_agxyz[5]

        print("lsm_ax: %-26s" % lsm_ax,
              "lsm_ay: %-26s" % lsm_ay,
              "lsm_az: %-26s" % lsm_az,
              "lsm_gx: %-26s" % lsm_gx,
              "lsm_gy: %-26s" % lsm_gy,
              "lsm_gz: %-26s\n" % lsm_gz,
              "mpu_ax: %-26s" % mpu_ax,
              "mpu_ay: %-26s" % mpu_ay,
              "mpu_az: %-26s" % mpu_az,
              "mpu_gx: %-26s" % mpu_gx,
              "mpu_gy: %-26s" % mpu_gy,
              "mpu_gz: %-26s\n" % mpu_gz,
              )
