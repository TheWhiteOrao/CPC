from math import fabs, atan2, asin, copysign, degrees


def euler_angle(Quaternion):

    # roll(x - axis rotation)
    sinr_cosp = +2.0 * (Quaternion["QuaternionR"] * Quaternion["QuaternionI"] + Quaternion["QuaternionJ"] * Quaternion["QuaternionK"])
    cosr_cosp = +1.0 - 2.0 * (Quaternion["QuaternionI"] * Quaternion["QuaternionI"] + Quaternion["QuaternionJ"] * Quaternion["QuaternionJ"])
    roll = atan2(sinr_cosp, cosr_cosp)

    # pitch(y - axis rotation)
    sinp = +2.0 * (Quaternion["QuaternionR"] * Quaternion["QuaternionJ"] - Quaternion["QuaternionK"] * Quaternion["QuaternionX"])
    if fabs(sinp) >= 1:
        pitch = copysign(M_PI / 2, sinp)
        # use 90 degrees if out of range
    else:
        pitch = asin(sinp)

    # yaw(z - axis rotation)
    siny_cosp = +2.0 * (Quaternion["QuaternionR"] * Quaternion["QuaternionK"] + Quaternion["QuaternionI"] * Quaternion["QuaternionJ"])
    cosy_cosp = +1.0 - 2.0 * (Quaternion["QuaternionJ"] * Quaternion["QuaternionJ"] + Quaternion["QuaternionK"] * Quaternion["QuaternionK"])
    yaw = atan2(siny_cosp, cosy_cosp)

    return degrees(roll), degrees(pitch), degrees(yaw)
