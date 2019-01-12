from math import fabs, atan2, asin, copysign


def euler_angle(Quaternion):

    # roll(x - axis rotation)
    sinr_cosp = +2.0 * (Quaternion["QuaternionW"] * Quaternion["QuaternionX"] + Quaternion["QuaternionY"] * Quaternion["QuaternionZ"])
    cosr_cosp = +1.0 - 2.0 * (Quaternion["QuaternionX"] * Quaternion["QuaternionX"] + Quaternion["QuaternionY"] * Quaternion["QuaternionY"])
    roll = atan2(sinr_cosp, cosr_cosp)

    # pitch(y - axis rotation)
    sinp = +2.0 * (Quaternion["QuaternionW"] * Quaternion["QuaternionY"] - Quaternion["QuaternionZ"] * Quaternion["QuaternionX"])
    if (fabs(sinp) >= 1)
        pitch = copysign(M_PI / 2, sinp)
        # use 90 degrees if out of range
    else
        pitch = asin(sinp)

    # yaw(z - axis rotation)
    siny_cosp = +2.0 * (Quaternion["QuaternionW"] * Quaternion["QuaternionZ"] + Quaternion["QuaternionX"] * Quaternion["QuaternionY"])
    cosy_cosp = +1.0 - 2.0 * (Quaternion["QuaternionY"] * Quaternion["QuaternionY"] + Quaternion["QuaternionZ"] * Quaternion["QuaternionZ"])
    yaw = atan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw
