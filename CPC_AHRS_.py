#
# Mahony AHRS algorithm implemented by Madgwick
# See: http:  # www.x - io.co.uk / node / 8  # open_source_ahrs_and_imu_algorithms
#
# Adapted by Igor Vereninov(igor.vereninov@emlid.com)
# Provided to you by Emlid Ltd(c) 2014.
# twitter.com / emlidtech | | www.emlid.com | | info@emlid.com
#


# include <cmath>
# include <stdio.h>
from math import *

q0 = 1
q1 = 0
q2 = 0
q3 = 0
twoKi = 0
twoKp = 2
gyroOffset = [0, 0, 0]
tr = 0


def update(ax, ay, az, gx,  gy,  gz,  mx,  my,  mz,  dt):
    global q0
    global q1
    global q2
    global q3

    # Use IMU algorithm if magnetometer measurement invalid(avoids NaN in magnetometer normalisation)
    if mx == 0 and my == 0 and mz == 0:
        updateIMU(gx, gy, gz, ax, ay, az, dt)

    # Compute feedback only if accelerometer measurement valid(avoids NaN in accelerometer normalisation)
    if not (ax == 0 and ay == 0 and az == 0):

        # Normalise accelerometer measurement
        recipNorm = (ax * ax + ay * ay + az * az) ** -0.5
        ax *= recipNorm
        ay *= recipNorm
        az *= recipNorm

        # Normalise magnetometer measurement
        recipNorm = (mx * mx + my * my + mz * mz) ** -0.5
        mx *= recipNorm
        my *= recipNorm
        mz *= recipNorm

        # Auxiliary variables to avoid repeated arithmetic
        q0q0 = q0 * q0
        q0q1 = q0 * q1
        q0q2 = q0 * q2
        q0q3 = q0 * q3
        q1q1 = q1 * q1
        q1q2 = q1 * q2
        q1q3 = q1 * q3
        q2q2 = q2 * q2
        q2q3 = q2 * q3
        q3q3 = q3 * q3

        # Reference direction of Earth's magnetic field
        hx = 2.0 * (mx * (0.5 - q2q2 - q3q3) + my * (q1q2 - q0q3) + mz * (q1q3 + q0q2))
        hy = 2.0 * (mx * (q1q2 + q0q3) + my * (0.5 - q1q1 - q3q3) + mz * (q2q3 - q0q1))
        bx = (hx * hx + hy * hy) ** 0.5
        bz = 2.0 * (mx * (q1q3 - q0q2) + my * (q2q3 + q0q1) + mz * (0.5 - q1q1 - q2q2))

        # Estimated direction of gravity and magnetic field
        halfvx = q1q3 - q0q2
        halfvy = q0q1 + q2q3
        halfvz = q0q0 - 0.5 + q3q3
        halfwx = bx * (0.5 - q2q2 - q3q3) + bz * (q1q3 - q0q2)
        halfwy = bx * (q1q2 - q0q3) + bz * (q0q1 + q2q3)
        halfwz = bx * (q0q2 + q1q3) + bz * (0.5 - q1q1 - q2q2)

        # Error is sum of cross product between estimated direction and measured direction of field vectors
        halfex = (ay * halfvz - az * halfvy) + (my * halfwz - mz * halfwy)
        halfey = (az * halfvx - ax * halfvz) + (mz * halfwx - mx * halfwz)
        halfez = (ax * halfvy - ay * halfvx) + (mx * halfwy - my * halfwx)

        # Compute and apply integral feedback if enabled
        if twoKi > 0:
            integralFBx += twoKi * halfex * dt  # integral error scaled by Ki
            integralFBy += twoKi * halfey * dt
            integralFBz += twoKi * halfez * dt
            gx += integralFBx  # apply integral feedback
            gy += integralFBy
            gz += integralFBz
        else:
            integralFBx = 0  # prevent integral windup
            integralFBy = 0
            integralFBz = 0

        # Apply proportional feedback
        gx += twoKp * halfex
        gy += twoKp * halfey
        gz += twoKp * halfez

    # Integrate rate of change of quaternion
    gx *= 0.5 * dt  # pre - multiply common factors
    gy *= 0.5 * dt
    gz *= 0.5 * dt
    qa = q0
    qb = q1
    qc = q2
    q0 += (-qb * gx - qc * gy - q3 * gz)
    q1 += (qa * gx + qc * gz - q3 * gy)
    q2 += (qa * gy - qb * gz + q3 * gx)
    q3 += (qa * gz + qb * gy - qc * gx)

    # Normalise quaternion
    recipNorm = (q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3) ** -0.5
    q0 *= recipNorm
    q1 *= recipNorm
    q2 *= recipNorm
    q3 *= recipNorm


def updateIMU(ax,  ay,  az,  gx,  gy,  gz,  dt):
    global q0
    global q1
    global q2
    global q3

    gx -= gyroOffset[0]
    gy -= gyroOffset[1]
    gz -= gyroOffset[2]

    # Compute feedback only if accelerometer measurement valid(avoids NaN in accelerometer normalisation)
    if not (ax == 0 and ay == 0 and az == 0):

        # Normalise accelerometer measurement
        recipNorm = (ax * ax + ay * ay + az * az) ** -0.5
        ax *= recipNorm
        ay *= recipNorm
        az *= recipNorm

        # Estimated direction of gravity and vector perpendicular to magnetic flux
        halfvx = q1 * q3 - q0 * q2
        halfvy = q0 * q1 + q2 * q3
        halfvz = q0 * q0 - 0.5 + q3 * q3

        # Error is sum of cross product between estimated and measured direction of gravity
        halfex = (ay * halfvz - az * halfvy)
        halfey = (az * halfvx - ax * halfvz)
        halfez = (ax * halfvy - ay * halfvx)

        # Compute and apply integral feedback if enabled
        if twoKi > 0:
            integralFBx += twoKi * halfex * dt  # integral error scaled by Ki
            integralFBy += twoKi * halfey * dt
            integralFBz += twoKi * halfez * dt
            gx += integralFBx  # apply integral feedback
            gy += integralFBy
            gz += integralFBz

        else:
            integralFBx = 0  # prevent integral windup
            integralFBy = 0
            integralFBz = 0

        # Apply proportional feedback
        gx += twoKp * halfex
        gy += twoKp * halfey
        gz += twoKp * halfez

    # Integrate rate of change of quaternion
    gx *= 0.5 * dt  # pre - multiply common factors
    gy *= 0.5 * dt
    gz *= 0.5 * dt
    qa = q0
    qb = q1
    qc = q2
    q0 += (-qb * gx - qc * gy - q3 * gz)
    q1 += (qa * gx + qc * gz - q3 * gy)
    q2 += (qa * gy - qb * gz + q3 * gx)
    q3 += (qa * gz + qb * gy - qc * gx)

    # Normalise quaternion
    recipNorm = (q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3) ** -0.5
    q0 *= recipNorm
    q1 *= recipNorm
    q2 *= recipNorm
    q3 *= recipNorm


def setGyroOffset(offsetX, offsetY, offsetZ):
    gyroOffset[0] = offsetX
    gyroOffset[1] = offsetY
    gyroOffset[2] = offsetZ


def getEuler():
    global tr

    roll = atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2)) * 180 / pi
    pitch = asin(2 * (q0 * q2 - q3 * q1)) * 180 / pi
    yaw = atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)) * 180 / pi
    # roll = atan2(2.0 * (q0 * q1 + q2 * q3), q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3) * 180 / pi
    # pitch = -asin(2.0 * (q1 * q3 - q0 * q2)) * 180 / pi
    # yaw = 0 + atan2(2.0 * (q0 * q3 + q1 * q2), q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3) * 180 / pi
    tr += q0
    print(yaw - tr)
    return roll, pitch, yaw


# endif # AHRS_hpp
# 0.054440907603739
# 0.054573651805083
# 0.057579213696842
