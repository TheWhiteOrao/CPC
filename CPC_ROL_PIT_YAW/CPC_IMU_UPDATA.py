from math import atan2
from cmath import asin


def imu_update(acc_sen,
               gyr_sen,
               delta_time,
               sen_gyr_offset,
               sen_quats):

    roll_pitch_quat_zer = sen_quats[0]
    roll_pitch_quat_one = sen_quats[1]
    roll_pitch_quat_two = sen_quats[2]
    roll_pitch_quat_thr = sen_quats[3]

    twoKp = 2

    acc_sen_x = acc_sen[0]
    acc_sen_y = acc_sen[1]
    acc_sen_z = acc_sen[2]

    roll_pitch_gyr_sen_x = gyr_sen[0]
    roll_pitch_gyr_sen_y = gyr_sen[1]
    roll_pitch_gyr_sen_z = gyr_sen[2]

    roll_pitch_gyr_sen_x -= sen_gyr_offset[0]
    roll_pitch_gyr_sen_y -= sen_gyr_offset[1]
    roll_pitch_gyr_sen_z -= sen_gyr_offset[2]

    if not (acc_sen_x == 0 and acc_sen_y == 0 and acc_sen_z == 0):

        # Normalise accelerometer measurement
        acc_norm = (acc_sen_x * acc_sen_x + acc_sen_y * acc_sen_y + acc_sen_z * acc_sen_z) ** 0.5
        acc_sen_x *= acc_norm
        acc_sen_y *= acc_norm
        acc_sen_z *= acc_norm

        # Normalise magnetometer measurement

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

        # Estimated direction of gravity and magnetic field
        roll_pitch_vx = roll_pitch_quat_one_thr - roll_pitch_quat_zer_two
        roll_pitch_vy = roll_pitch_quat_zer_one + roll_pitch_quat_two_thr
        roll_pitch_vz = roll_pitch_quat_zer_zer - 0.5 + roll_pitch_quat_thr_thr

        # Error is sum of cross product between estimated and measured direction of gravity
        roll_pitch_ex = (acc_sen_y * roll_pitch_vz - acc_sen_z * roll_pitch_vy)
        roll_pitch_ey = (acc_sen_z * roll_pitch_vx - acc_sen_x * roll_pitch_vz)
        roll_pitch_ez = (acc_sen_x * roll_pitch_vy - acc_sen_y * roll_pitch_vx)

        # Apply proportional feedback
        roll_pitch_gyr_sen_x += twoKp * roll_pitch_ex
        roll_pitch_gyr_sen_y += twoKp * roll_pitch_ey
        roll_pitch_gyr_sen_z += twoKp * roll_pitch_ez

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

        # Normalise quaternion
        roll_pitch_quat_norm = (roll_pitch_quat_zer * roll_pitch_quat_zer + roll_pitch_quat_one * roll_pitch_quat_one + roll_pitch_quat_two * roll_pitch_quat_two + roll_pitch_quat_thr * roll_pitch_quat_thr) ** 0.5
        roll_pitch_quat_zer *= roll_pitch_quat_norm
        roll_pitch_quat_one *= roll_pitch_quat_norm
        roll_pitch_quat_two *= roll_pitch_quat_norm
        roll_pitch_quat_thr *= roll_pitch_quat_norm

        return [roll_pitch_quat_zer,
                roll_pitch_quat_one,
                roll_pitch_quat_two,
                roll_pitch_quat_thr]


def get_euler(sen_quats):

    roll_pitch_quat_zer = sen_quats[0]
    roll_pitch_quat_one = sen_quats[1]
    roll_pitch_quat_two = sen_quats[2]
    roll_pitch_quat_thr = sen_quats[3]

    pitch = atan2(2 * (roll_pitch_quat_zer * roll_pitch_quat_one + roll_pitch_quat_two * roll_pitch_quat_thr), 1 - 2 * (roll_pitch_quat_one * roll_pitch_quat_one + roll_pitch_quat_two * roll_pitch_quat_two)) * 180 / pi
    roll = asin(2 * (roll_pitch_quat_zer * roll_pitch_quat_two - roll_pitch_quat_thr * roll_pitch_quat_one)) * 180 / pi

    return roll, pitch
