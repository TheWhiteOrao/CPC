from math import *

twoKp = 2


def imu_update(acc_sen,
               gyr_sen,
               mag_sen,
               delta_time,
               sen_gyr_offset,
               sen_quats):

    roll_pitch_quat_zer = sen_quats[0]
    roll_pitch_quat_one = sen_quats[1]
    roll_pitch_quat_two = sen_quats[2]
    roll_pitch_quat_thr = sen_quats[3]
    yaw_quat_zer = sen_quats[4]
    yaw_quat_one = sen_quats[5]
    yaw_quat_two = sen_quats[6]
    yaw_quat_thr = sen_quats[7]

    global twoKp

    acc_sen_x = acc_sen[0]
    acc_sen_y = acc_sen[1]
    acc_sen_z = acc_sen[2]

    roll_pitch_gyr_sen_x = gyr_sen[0]
    roll_pitch_gyr_sen_y = gyr_sen[1]
    roll_pitch_gyr_sen_z = gyr_sen[2]

    yaw_gyr_sen_x = gyr_sen[0]
    yaw_gyr_sen_y = gyr_sen[1]
    yaw_gyr_sen_z = gyr_sen[2]

    mag_sen_x = mag_sen[0]
    mag_sen_y = mag_sen[1]
    mag_sen_z = mag_sen[2]

    roll_pitch_gyr_sen_x -= sen_gyr_offset[0]
    roll_pitch_gyr_sen_y -= sen_gyr_offset[1]
    roll_pitch_gyr_sen_z -= sen_gyr_offset[2]

    yaw_gyr_sen_x -= sen_gyr_offset[0]
    yaw_gyr_sen_y -= sen_gyr_offset[1]
    yaw_gyr_sen_z -= sen_gyr_offset[2]

    if not (acc_sen_x == 0 and acc_sen_y == 0 and acc_sen_z == 0):

        # Normalise accelerometer measurement
        acc_norm = (acc_sen_x * acc_sen_x + acc_sen_y * acc_sen_y + acc_sen_z * acc_sen_z) ** -0.5
        acc_sen_x *= acc_norm
        acc_sen_y *= acc_norm
        acc_sen_z *= acc_norm

        # Normalise magnetometer measurement
        if not (mag_sen_x == 0 and mag_sen_y == 0 and mag_sen_z == 0)
            mag_norm = (mag_sen_x * mag_sen_x + mag_sen_y * mag_sen_y + mag_sen_z * mag_sen_z) ** -0.5
            mag_sen_x *= mag_norm
            mag_sen_y *= mag_norm
            mag_sen_z *= mag_norm

        # Auxiliary variables to avoid repeated arithmetic
        roll_pitch_quat_zer_zer = roll_pitch_quat_zer * roll_pitch_quat_zer
        roll_pitch_quat_zer_one = roll_pitch_quat_zer * roll_pitch_quat_one
        roll_pitch_quat_zer_two = roll_pitch_quat_zer * roll_pitch_quat_two
        roll_pitch_quat_zer_thr = roll_pitch_quat_zer * roll_pitch_quat_thr
        roll_pitch_quat_one_one = roll_pitch_quat_one * roll_pitch_quat_one
        roll_pitch_quat_one_two = roll_pitch_quat_one * roll_pitch_quat_two
        roll_pitch_quat_one_thr = roll_pitch_quat_one * roll_pitch_quat_thr
        roll_pitch_quat_two_two = roll_pitch_quat_two * roll_pitch_quat_two
        roll_pitch_quat_two_thr = roll_pitch_quat_two * roll_pitch_quat_thr
        roll_pitch_quat_thr_thr = roll_pitch_quat_thr * roll_pitch_quat_thr

        if not (mag_sen_x == 0 and mag_sen_y == 0 and mag_sen_z == 0):
            yaw_quat_zer_zer = yaw_quat_zer * yaw_quat_zer
            yaw_quat_zer_one = yaw_quat_zer * yaw_quat_one
            yaw_quat_zer_two = yaw_quat_zer * yaw_quat_two
            yaw_quat_zer_thr = yaw_quat_zer * yaw_quat_thr
            yaw_quat_one_one = yaw_quat_one * yaw_quat_one
            yaw_quat_one_two = yaw_quat_one * yaw_quat_two
            yaw_quat_one_thr = yaw_quat_one * yaw_quat_thr
            yaw_quat_two_two = yaw_quat_two * yaw_quat_two
            yaw_quat_two_thr = yaw_quat_two * yaw_quat_thr
            yaw_quat_thr_thr = yaw_quat_thr * yaw_quat_thr

        # Reference direction of Earth's magnetic field
        if not (mag_sen_x == 0 and mag_sen_y == 0 and mag_sen_z == 0):
            yaw_hx = 2 * (mag_sen_x * (0.5 - yaw_quat_two_two - yaw_quat_thr_thr) + mag_sen_y * (yaw_quat_one_two - yaw_quat_zer_thr) + mag_sen_z * (yaw_quat_one_thr + yaw_quat_zer_two))
            yaw_hy = 2 * (mag_sen_x * (yaw_quat_one_two + yaw_quat_zer_thr) + mag_sen_y * (0.5 - yaw_quat_one_one - yaw_quat_thr_thr) + mag_sen_z * (yaw_quat_two_thr - yaw_quat_zer_one))
            yaw_bx = (yaw_hx * yaw_hx + yaw_hy * yaw_hy) ** 0.5
            yaw_bz = 2 * (mag_sen_x * (yaw_quat_one_thr - yaw_quat_zer_two) + mag_sen_y * (yaw_quat_two_thr + yaw_quat_zer_one) + mag_sen_z * (0.5 - yaw_quat_one_one - yaw_quat_two_two))

        # Estimated direction of gravity and magnetic field
        roll_pitch_vx = roll_pitch_quat_one_thr - roll_pitch_quat_zer_two
        roll_pitch_vy = roll_pitch_quat_zer_one + roll_pitch_quat_two_thr
        roll_pitch_vz = roll_pitch_quat_zer_zer - 0.5 + roll_pitch_quat_thr_thr

        if not (mag_sen_x == 0 and mag_sen_y == 0 and mag_sen_z == 0):
            yaw_vx = yaw_quat_one_thr - yaw_quat_zer_two
            yaw_vy = yaw_quat_zer_one + yaw_quat_two_thr
            yaw_vz = yaw_quat_zer_zer - 0.5 + yaw_quat_thr_thr

            yaw_wx = yaw_bx * (0.5 - yaw_quat_two_two - yaw_quat_thr_thr) + yaw_bz * (yaw_quat_one_thr - yaw_quat_zer_two)
            yaw_wy = yaw_bx * (yaw_quat_one_two - yaw_quat_zer_thr) + yaw_bz * (yaw_quat_zer_one + yaw_quat_two_thr)
            yaw_wz = yaw_bx * (yaw_quat_zer_two + yaw_quat_one_thr) + yaw_bz * (0.5 - yaw_quat_one_one - yaw_quat_two_two)

        # Error is sum of cross product between estimated and measured direction of gravity
        roll_pitch_ex = (acc_sen_y * roll_pitch_vz - acc_sen_z * roll_pitch_vy)
        roll_pitch_ey = (acc_sen_z * roll_pitch_vx - acc_sen_x * roll_pitch_vz)
        roll_pitch_ez = (acc_sen_x * roll_pitch_vy - acc_sen_y * roll_pitch_vx)

        if not (mag_sen_x == 0 and mag_sen_y == 0 and mag_sen_z == 0):
            yaw_ex = (acc_sen_y * yaw_vz - acc_sen_z * yaw_vy) + (mag_sen_y * yaw_wz - mag_sen_z * yaw_wy)
            yaw_ey = (acc_sen_z * yaw_vx - acc_sen_x * yaw_vz) + (mag_sen_z * yaw_wx - mag_sen_x * yaw_wz)
            yaw_ez = (acc_sen_x * yaw_vy - acc_sen_y * yaw_vx) + (mag_sen_x * yaw_wy - mag_sen_y * yaw_wx)

        # Compute and apply integral feedback if enabled

        # Apply proportional feedback
        roll_pitch_gyr_sen_x += twoKp * roll_pitch_ex
        roll_pitch_gyr_sen_y += twoKp * roll_pitch_ey
        roll_pitch_gyr_sen_z += twoKp * roll_pitch_ez

        if not (mag_sen_x == 0 and mag_sen_y == 0 and mag_sen_z == 0):
            yaw_gyr_sen_x += twoKp * yaw_ex
            yaw_gyr_sen_y += twoKp * yaw_ey
            yaw_gyr_sen_z += twoKp * yaw_ez

        # Integrate rate of change of quaternion
        roll_pitch_gyr_sen_x *= 0.5 * delta_time  # pre - multiply common factors
        roll_pitch_gyr_sen_y *= 0.5 * delta_time
        roll_pitch_gyr_sen_z *= 0.5 * delta_time
        roll_pitch_quat_a = roll_pitch_quat_zer
        roll_pitch_quat_b = roll_pitch_quat_one
        roll_pitch_quat_c = roll_pitch_quat_two
        roll_pitch_quat_zer += (-roll_pitch_quat_b * roll_pitch_gyr_sen_x - roll_pitch_quat_c * roll_pitch_gyr_sen_y - roll_pitch_quat_thr * roll_pitch_gyr_sen_z)
        roll_pitch_quat_one += (roll_pitch_quat_a * roll_pitch_gyr_sen_x + roll_pitch_quat_c * roll_pitch_gyr_sen_z - roll_pitch_quat_thr * roll_pitch_gyr_sen_y)
        roll_pitch_quat_two += (roll_pitch_quat_a * roll_pitch_gyr_sen_y - roll_pitch_quat_b * roll_pitch_gyr_sen_z + roll_pitch_quat_thr * roll_pitch_gyr_sen_x)
        roll_pitch_quat_thr += (roll_pitch_quat_a * roll_pitch_gyr_sen_z + roll_pitch_quat_b * roll_pitch_gyr_sen_y - roll_pitch_quat_c * roll_pitch_gyr_sen_x)

        if not (mag_sen_x == 0 and mag_sen_y == 0 and mag_sen_z == 0):
            yaw_gyr_sen_x *= 0.5 * delta_time  # pre - multiply common factors
            yaw_gyr_sen_y *= 0.5 * delta_time
            yaw_gyr_sen_z *= 0.5 * delta_time
            yaw_quat_a = yaw_quat_zer
            yaw_quat_b = yaw_quat_one
            yaw_quat_c = yaw_quat_two
            yaw_quat_zer += (-yaw_quat_b * yaw_gyr_sen_x - yaw_quat_c * yaw_gyr_sen_y - yaw_quat_thr * yaw_gyr_sen_z)
            yaw_quat_one += (yaw_quat_a * yaw_gyr_sen_x + yaw_quat_c * yaw_gyr_sen_z - yaw_quat_thr * yaw_gyr_sen_y)
            yaw_quat_two += (yaw_quat_a * yaw_gyr_sen_y - yaw_quat_b * yaw_gyr_sen_z + yaw_quat_thr * yaw_gyr_sen_x)
            yaw_quat_thr += (yaw_quat_a * yaw_gyr_sen_z + yaw_quat_b * yaw_gyr_sen_y - yaw_quat_c * yaw_gyr_sen_x)

        # Normalise quaternion
        roll_pitch_quat_norm = (roll_pitch_quat_zer * roll_pitch_quat_zer + roll_pitch_quat_one * roll_pitch_quat_one + roll_pitch_quat_two * roll_pitch_quat_two + roll_pitch_quat_thr * roll_pitch_quat_thr) ** -0.5
        roll_pitch_quat_zer *= roll_pitch_quat_norm
        roll_pitch_quat_one *= roll_pitch_quat_norm
        roll_pitch_quat_two *= roll_pitch_quat_norm
        roll_pitch_quat_thr *= roll_pitch_quat_norm

        if not (mag_sen_x == 0 and mag_sen_y == 0 and mag_sen_z == 0):
            yaw_quat_norm = (yaw_quat_zer * yaw_quat_zer + yaw_quat_one * yaw_quat_one + yaw_quat_two * yaw_quat_two + yaw_quat_thr * yaw_quat_thr) ** -0.5
            yaw_quat_zer *= yaw_quat_norm
            yaw_quat_one *= yaw_quat_norm
            yaw_quat_two *= yaw_quat_norm
            yaw_quat_thr *= yaw_quat_norm

        return [roll_pitch_quat_zer,
                roll_pitch_quat_one,
                roll_pitch_quat_two,
                roll_pitch_quat_thr,
                yaw_quat_zer,
                yaw_quat_one,
                yaw_quat_two,
                yaw_quat_thr]


def get_euler(sen_quats):

    roll_pitch_quat_zer = sen_quats[0]
    roll_pitch_quat_one = sen_quats[1]
    roll_pitch_quat_two = sen_quats[2]
    roll_pitch_quat_thr = sen_quats[3]
    yaw_quat_zer = sen_quats[4]
    yaw_quat_one = sen_quats[5]
    yaw_quat_two = sen_quats[6]
    yaw_quat_thr = sen_quats[7]

    roll = atan2(2 * (roll_pitch_quat_zer * roll_pitch_quat_one + roll_pitch_quat_two * roll_pitch_quat_thr), 1 - 2 * (roll_pitch_quat_one * roll_pitch_quat_one + roll_pitch_quat_two * roll_pitch_quat_two)) * 180 / pi
    pitch = asin(2 * (roll_pitch_quat_zer * roll_pitch_quat_two - roll_pitch_quat_thr * roll_pitch_quat_one)) * 180 / pi
    yaw = atan2(2 * (yaw_quat_zer * yaw_quat_thr + yaw_quat_one * yaw_quat_two), 1 - 2 * (yaw_quat_two * yaw_quat_two + yaw_quat_thr * yaw_quat_thr)) * 180 / pi

    return roll, pitch, yaw
