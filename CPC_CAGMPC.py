from CPC_NAVIO2.lsm9ds1 import *
from CPC_NAVIO2.mpu9250 import *
from time import *

lsm9ds1 = LSM9DS1()
mpu9250 = MPU9250()

lsm9ds1.initialize()
mpu9250.initialize()

lsm_offset = [0, 0, 0]
mpu_offset = [0, 0, 0]
PI = 3.14159265
q0 = 1
q1 = 0
q2 = 0
q3 = 0


def usleep(x):
    return sleep(x / 1000000.0)


for i in range(1000):
    lsm_axyz, lsm_gxyz = lsm9ds1.getMotion6()
    mpu_axyz, mpu_gxyz = mpu9250.getMotion6()

    lsm_gx = round(lsm_gxyz[0], 8)
    lsm_gy = round(lsm_gxyz[1], 8)
    lsm_gz = round(lsm_gxyz[2], 8)

    mpu_gx = round(mpu_gxyz[0], 8)
    mpu_gy = round(mpu_gxyz[1], 8)
    mpu_gz = round(mpu_gxyz[2], 8)

    lsm_gx *= 180 / PI
    lsm_gy *= 180 / PI
    lsm_gz *= 180 / PI

    mpu_gx *= 180 / PI
    mpu_gy *= 180 / PI
    mpu_gz *= 180 / PI

    lsm_offset[0] += (-lsm_gx * 0.0175)
    lsm_offset[1] += (-lsm_gy * 0.0175)
    lsm_offset[2] += (-lsm_gz * 0.0175)

    mpu_offset[0] += (-mpu_gx * 0.0175)
    mpu_offset[1] += (-mpu_gy * 0.0175)
    mpu_offset[2] += (-mpu_gz * 0.0175)

    usleep(10000)

lsm_offset[0] /= 1000
lsm_offset[1] /= 1000
lsm_offset[2] /= 1000

mpu_offset[0] /= 1000
mpu_offset[1] /= 1000
mpu_offset[2] /= 1000

while True:

    lsm_axyz, lsm_gxyz = lsm9ds1.getMotion6()
    mpu_axyz, mpu_gxyz = mpu9250.getMotion6()

    lsm_ax = round(lsm_axyz[0], 8)
    lsm_ay = round(lsm_axyz[1], 8)
    lsm_az = round(lsm_axyz[2], 8)
    lsm_gx = round(lsm_gxyz[0], 8)
    lsm_gy = round(lsm_gxyz[1], 8)
    lsm_gz = round(lsm_gxyz[2], 8)

    mpu_ax = round(mpu_axyz[0], 8)
    mpu_ay = round(mpu_axyz[1], 8)
    mpu_az = round(mpu_axyz[2], 8)
    mpu_gx = round(mpu_gxyz[0], 8)
    mpu_gy = round(mpu_gxyz[1], 8)
    mpu_gz = round(mpu_gxyz[2], 8)

    lsm_gx -= lsm_offset[0]
    lsm_gy -= lsm_offset[1]
    lsm_gz -= lsm_offset[2]

    mpu_gx -= mpu_offset[0]
    mpu_gy -= mpu_offset[1]
    mpu_gz -= mpu_offset[2]

    if not (lsm_ax == 0 and lsm_ay == 0 and lsm_az == 0):

        # Normalise accelerometer measurement
        recipNorm = (lsm_ax * lsm_ax + lsm_ay * lsm_ay + lsm_az * lsm_az) ** -0.5
        lsm_ax *= recipNorm
        lsm_ay *= recipNorm
        lsm_az *= recipNorm

    if not (mpu_ax == 0 and mpu_ay == 0 and mpu_az == 0):

        # Normalise accelerometer measurement
        recipNorm = (mpu_ax * mpu_ax + mpu_ay * mpu_ay + mpu_az * mpu_az) ** -0.5
        mpu_ax *= recipNorm
        mpu_ay *= recipNorm
        mpu_az *= recipNorm

    print("lsm_offset: %-26s" % lsm_offset[0],
          "lsm_offset: %-26s" % lsm_offset[1],
          "lsm_offset: %-26s" % lsm_offset[2],
          "mpu_offset: %-26s" % mpu_offset[0],
          "mpu_offset: %-26s" % mpu_offset[1],
          "mpu_offset: %-26s" % mpu_offset[2])

    print("lsm_ax: %-26s" % lsm_ax,
          "lsm_ay: %-26s" % lsm_ay,
          "lsm_az: %-26s" % lsm_az,
          "lsm_gx: %-26s" % lsm_gx,
          "lsm_gy: %-26s" % lsm_gy,
          "lsm_gz: %-26s" % lsm_gz)

    print("mpu_ax: %-26s" % mpu_ax,
          "mpu_ay: %-26s" % mpu_ay,
          "mpu_az: %-26s" % mpu_az,
          "mpu_gx: %-26s" % mpu_gx,
          "mpu_gy: %-26s" % mpu_gy,
          "mpu_gz: %-26s" % mpu_gz)

    print("  d_ax: %-26s" % ((lsm_ax + mpu_ax) / 2),
          "  d_ay: %-26s" % ((lsm_ay + mpu_ay) / 2),
          "  d_az: %-26s" % ((lsm_az + mpu_az) / 2),
          "  d_gx: %-26s" % ((lsm_gx + mpu_gx) / 2),
          "  d_gy: %-26s" % ((lsm_gy + mpu_gy) / 2),
          "  d_gz: %-26s" % ((lsm_gz + mpu_gz) / 2))

    print("\n")
    sleep(0.1)
