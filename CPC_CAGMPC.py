from CPC_NAVIO2.lsm9ds1 import *
from CPC_NAVIO2.mpu9250 import *
from time import *

lsm9ds1 = LSM9DS1()
mpu9250 = MPU9250()

lsm9ds1.initialize()
mpu9250.initialize()

while True:

    lsm_axyz, lsm_gxyz = lsm9ds1.getMotion6()
    mpu_axyz, mpu_gxyz = mpu9250.getMotion6()

    lsm_ax = lsm_axyz[0]
    lsm_ay = lsm_axyz[1]
    lsm_az = lsm_axyz[2]
    lsm_gx = lsm_gxyz[0]
    lsm_gy = lsm_gxyz[1]
    lsm_gz = lsm_gxyz[2]

    mpu_ax = mpu_axyz[0]
    mpu_ay = mpu_axyz[1]
    mpu_az = mpu_axyz[2]
    mpu_gx = mpu_gxyz[0]
    mpu_gy = mpu_gxyz[1]
    mpu_gz = mpu_gxyz[2]

    print("lsm_ax: %-26s" % round(lsm_ax, 8),
          "lsm_ay: %-26s" % round(lsm_ay, 8),
          "lsm_az: %-26s" % round(lsm_az, 8),
          "lsm_gx: %-26s" % round(lsm_gx, 8),
          "lsm_gy: %-26s" % round(lsm_gy, 8),
          "lsm_gz: %-26s" % round(lsm_gz, 8))

    print("mpu_ax: %-26s" % round(mpu_ax, 8),
          "mpu_ay: %-26s" % round(mpu_ay, 8),
          "mpu_az: %-26s" % round(mpu_az, 8),
          "mpu_gx: %-26s" % round(mpu_gx, 8),
          "mpu_gy: %-26s" % round(mpu_gy, 8),
          "mpu_gz: %-26s" % round(mpu_gz, 8))

    print("  d_ax: %-26s" % round((lsm_ax + mpu_ax) / 2, 8),
          "  d_ay: %-26s" % round((lsm_ay + mpu_ay) / 2, 8),
          "  d_az: %-26s" % round((lsm_az + mpu_az) / 2, 8),
          "  d_gx: %-26s" % round((lsm_gx + mpu_gx) / 2, 8),
          "  d_gy: %-26s" % round((lsm_gy + mpu_gy) / 2, 8),
          "  d_gz: %-26s" % round((lsm_gz + mpu_gz) / 2, 8))
    print("\n")
    sleep(0.1)
