from CPC_NAVIO2.lsm9ds1 import *
from CPC_NAVIO2.mpu9250 import *
from time import *
from math import *

lsm9ds1 = LSM9DS1()
mpu9250 = MPU9250()

lsm9ds1.initialize()
mpu9250.initialize()

lsm_offset = [0, 0, 0]
mpu_offset = [0, 0, 0]
PI = 3.14159265
G_SI = 9.80665

currenttime = 0


lsm_twoKi = 0
lsm_twoKp = 2

mpu_twoKi = 0
mpu_twoKp = 2

lsm_q0 = 1
lsm_q1 = 0
lsm_q2 = 0
lsm_q3 = 0

mpu_q0 = 1
mpu_q1 = 0
mpu_q2 = 0
mpu_q3 = 0

lsm_integralFBx = 0
lsm_integralFBy = 0
lsm_integralFBz = 0

mpu_integralFBx = 0
mpu_integralFBy = 0
mpu_integralFBz = 0


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

    previoustime = currenttime
    currenttime = time_ns()

    lsm_dt = (currenttime - previoustime) / 1000000000
    mpu_dt = (currenttime - previoustime) / 1000000000

    if (lsm_dt + mpu_dt) / 2 < (1 / 1300):
        usleep((1 / 1300 - (lsm_dt + mpu_dt) / 2) * 1000000)
        currenttime = time_ns()

    lsm_dt = (currenttime - previoustime) / 1000000000
    mpu_dt = (currenttime - previoustime) / 1000000000

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

    lsm_ax /= G_SI
    lsm_ay /= G_SI
    lsm_az /= G_SI
    lsm_gx *= 180 / PI
    lsm_gy *= 180 / PI
    lsm_gz *= 180 / PI

    lsm_gx *= 0.0175
    lsm_gy *= 0.0175
    lsm_gz *= 0.0175

    mpu_ax /= G_SI
    mpu_ay /= G_SI
    mpu_az /= G_SI
    mpu_gx *= 180 / PI
    mpu_gy *= 180 / PI
    mpu_gz *= 180 / PI

    mpu_gx *= 0.0175
    mpu_gy *= 0.0175
    mpu_gz *= 0.0175

    lsm_gx -= lsm_offset[0]
    lsm_gy -= lsm_offset[1]
    lsm_gz -= lsm_offset[2]

    mpu_gx -= mpu_offset[0]
    mpu_gy -= mpu_offset[1]
    mpu_gz -= mpu_offset[2]

    if not (lsm_ax == 0 and lsm_ay == 0 and lsm_az == 0):

        # Normalise accelerometer measurement
        lsm_recipNorm = (lsm_ax * lsm_ax + lsm_ay * lsm_ay + lsm_az * lsm_az) ** -0.5
        lsm_ax *= lsm_recipNorm
        lsm_ay *= lsm_recipNorm
        lsm_az *= lsm_recipNorm

        lsm_q0q0 = lsm_q0 * lsm_q0
        lsm_q0q1 = lsm_q0 * lsm_q1
        lsm_q0q2 = lsm_q0 * lsm_q2
        lsm_q0q3 = lsm_q0 * lsm_q3
        lsm_q1q1 = lsm_q1 * lsm_q1
        lsm_q1q2 = lsm_q1 * lsm_q2
        lsm_q1q3 = lsm_q1 * lsm_q3
        lsm_q2q2 = lsm_q2 * lsm_q2
        lsm_q2q3 = lsm_q2 * lsm_q3
        lsm_q3q3 = lsm_q3 * lsm_q3

        lsm_halfvx = lsm_q1q3 - lsm_q0q2
        lsm_halfvy = lsm_q0q1 + lsm_q2q3
        lsm_halfvz = lsm_q0q0 - 0.5 + lsm_q3q3

        lsm_halfex = (lsm_ay * lsm_halfvz - lsm_az * lsm_halfvy)
        lsm_halfey = (lsm_az * lsm_halfvx - lsm_ax * lsm_halfvz)
        lsm_halfez = (lsm_ax * lsm_halfvy - lsm_ay * lsm_halfvx)

        if lsm_twoKi > 0:
            lsm_integralFBx += lsm_twoKi * lsm_halfex * lsm_dt
            lsm_integralFBy += lsm_twoKi * lsm_halfey * lsm_dt
            lsm_integralFBz += lsm_twoKi * lsm_halfez * lsm_dt
            lsm_gx += lsm_integralFBx
            lsm_gy += lsm_integralFBy
            lsm_gz += lsm_integralFBz

        else:
            lsm_integralFBx = 0
            lsm_integralFBy = 0
            lsm_integralFBz = 0

        lsm_gx += lsm_twoKp * lsm_halfex
        lsm_gy += lsm_twoKp * lsm_halfey
        lsm_gz += lsm_twoKp * lsm_halfez

    lsm_gx *= 0.5 * lsm_dt
    lsm_gy *= 0.5 * lsm_dt
    lsm_gz *= 0.5 * lsm_dt
    lsm_qa = lsm_q0
    lsm_qb = lsm_q1
    lsm_qc = lsm_q2
    lsm_q0 += (-lsm_qb * lsm_gx - lsm_qc * lsm_gy - lsm_q3 * lsm_gz)
    lsm_q1 += (lsm_qa * lsm_gx + lsm_qc * lsm_gz - lsm_q3 * lsm_gy)
    lsm_q2 += (lsm_qa * lsm_gy - lsm_qb * lsm_gz + lsm_q3 * lsm_gx)
    lsm_q3 += (lsm_qa * lsm_gz + lsm_qb * lsm_gy - lsm_qc * lsm_gx)
    lsm_recipNorm = (lsm_q0 * lsm_q0 + lsm_q1 * lsm_q1 + lsm_q2 * lsm_q2 + lsm_q3 * lsm_q3) ** -0.5
    lsm_q0 *= lsm_recipNorm
    lsm_q1 *= lsm_recipNorm
    lsm_q2 *= lsm_recipNorm
    lsm_q3 *= lsm_recipNorm

    lsm_roll = atan2(2 * (lsm_q0 * lsm_q1 + lsm_q2 * lsm_q3), 1 - 2 * (lsm_q1 * lsm_q1 + lsm_q2 * lsm_q2)) * 180 / PI
    lsm_PItch = asin(2 * (lsm_q0 * lsm_q2 - lsm_q3 * lsm_q1)) * 180 / PI
    lsm_yaw = atan2(2 * (lsm_q0 * lsm_q3 + lsm_q1 * lsm_q2), 1 - 2 * (lsm_q2 * lsm_q2 + lsm_q3 * lsm_q3)) * 180 / PI

    if not (mpu_ax == 0 and mpu_ay == 0 and mpu_az == 0):

        # Normalise accelerometer measurement
        recipNorm = (mpu_ax * mpu_ax + mpu_ay * mpu_ay + mpu_az * mpu_az) ** -0.5
        mpu_ax *= recipNorm
        mpu_ay *= recipNorm
        mpu_az *= recipNorm

        mpu_q0q0 = mpu_q0 * mpu_q0
        mpu_q0q1 = mpu_q0 * mpu_q1
        mpu_q0q2 = mpu_q0 * mpu_q2
        mpu_q0q3 = mpu_q0 * mpu_q3
        mpu_q1q1 = mpu_q1 * mpu_q1
        mpu_q1q2 = mpu_q1 * mpu_q2
        mpu_q1q3 = mpu_q1 * mpu_q3
        mpu_q2q2 = mpu_q2 * mpu_q2
        mpu_q2q3 = mpu_q2 * mpu_q3
        mpu_q3q3 = mpu_q3 * mpu_q3

        mpu_halfvx = mpu_q1q3 - mpu_q0q2
        mpu_halfvy = mpu_q0q1 + mpu_q2q3
        mpu_halfvz = mpu_q0q0 - 0.5 + mpu_q3q3

        mpu_halfex = (mpu_ay * mpu_halfvz - mpu_az * mpu_halfvy)
        mpu_halfey = (mpu_az * mpu_halfvx - mpu_ax * mpu_halfvz)
        mpu_halfez = (mpu_ax * mpu_halfvy - mpu_ay * mpu_halfvx)

        if mpu_twoKi > 0:
            mpu_integralFBx += mpu_twoKi * mpu_halfex * mpu_dt
            mpu_integralFBy += mpu_twoKi * mpu_halfey * mpu_dt
            mpu_integralFBz += mpu_twoKi * mpu_halfez * mpu_dt
            mpu_gx += mpu_integralFBx
            mpu_gy += mpu_integralFBy
            mpu_gz += mpu_integralFBz

        else:
            mpu_integralFBx = 0
            mpu_integralFBy = 0
            mpu_integralFBz = 0

        mpu_gx += mpu_twoKp * mpu_halfex
        mpu_gy += mpu_twoKp * mpu_halfey
        mpu_gz += mpu_twoKp * mpu_halfez

    mpu_gx *= 0.5 * mpu_dt
    mpu_gy *= 0.5 * mpu_dt
    mpu_gz *= 0.5 * mpu_dt
    mpu_qa = mpu_q0
    mpu_qb = mpu_q1
    mpu_qc = mpu_q2
    mpu_q0 += (-mpu_qb * mpu_gx - mpu_qc * mpu_gy - mpu_q3 * mpu_gz)
    mpu_q1 += (mpu_qa * mpu_gx + mpu_qc * mpu_gz - mpu_q3 * mpu_gy)
    mpu_q2 += (mpu_qa * mpu_gy - mpu_qb * mpu_gz + mpu_q3 * mpu_gx)
    mpu_q3 += (mpu_qa * mpu_gz + mpu_qb * mpu_gy - mpu_qc * mpu_gx)
    mpu_recipNorm = (mpu_q0 * mpu_q0 + mpu_q1 * mpu_q1 + mpu_q2 * mpu_q2 + mpu_q3 * mpu_q3) ** -0.5
    mpu_q0 *= mpu_recipNorm
    mpu_q1 *= mpu_recipNorm
    mpu_q2 *= mpu_recipNorm
    mpu_q3 *= mpu_recipNorm

    mpu_roll = atan2(2 * (mpu_q0 * mpu_q1 + mpu_q2 * mpu_q3), 1 - 2 * (mpu_q1 * mpu_q1 + mpu_q2 * mpu_q2)) * 180 / PI
    mpu_PItch = asin(2 * (mpu_q0 * mpu_q2 - mpu_q3 * mpu_q1)) * 180 / PI
    mpu_yaw = atan2(2 * (mpu_q0 * mpu_q3 + mpu_q1 * mpu_q2), 1 - 2 * (mpu_q2 * mpu_q2 + mpu_q3 * mpu_q3)) * 180 / PI

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

    print("lsm_roll  : %-26s" % lsm_roll,
          "lsm_PItch  : %-26s" % lsm_PItch,
          "lsm_yaw  : %-26s" % lsm_yaw,
          "mpu_roll  : %-26s" % mpu_roll,
          "mpu_PItch  : %-26s" % mpu_PItch,
          "mpu_yaw  : %-26s" % mpu_yaw)

    print(lsm_yaw + mpu_yaw)
    print("\n")
    sleep(0.1)
