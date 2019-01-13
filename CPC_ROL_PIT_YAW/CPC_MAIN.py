from time import *
from CPC_NA2.mpu9250 import *
# from CPC_NA2.lsm9ds1 import *
from CPC_SENSORS_READ import sensor_read
from CPC_GYRO_CALI import gyroscope_calibration
from CPC_DELTA_TIME import delta_time_calculate
from CPC_IMU_UPDATA import *
from CPC_LED_DATA import *

mpu9250 = MPU9250()
# lsm9ds1 = LSM9DS1()

mpu_gyr_offset = 0
# lsm_gyr_offset = 0
prev_time = 0
dtsumm = 0
temp_mpu_roll = 0
temp_mpu_pitch = 0
# temp_lsm_roll = 0
# temp_lsm_pitch = 0

mpu_quats = [1, 0, 0, 0,
             1, 0, 0, 0]

# lsm_quats = [1, 0, 0, 0,
#              1, 0, 0, 0]


def offset_setup():
    global mpu_gyr_offset
    # global lsm_gyr_offset

    led_singel("Red")

    # ---------------------------- Sensors Initialize ---------------------------- #

    # print("Initialize of mpu9250 and lsm9ds1 sensors starts.")

    mpu9250.initialize()
    # lsm9ds1.initialize()

    # print("Initialize of mpu9250 and lsm9ds1 sensors is done.\n")

    # ---------------------------------------------------------------------------- #
    # ----------------------------- Gyro Calibration ----------------------------- #

    # print("Calibration the Gyro.")

    mpu_gyr_offset = gyroscope_calibration(mpu9250)
    # lsm_gyr_offset = gyroscope_calibration(lsm9ds1)

    # print(mpu_gyr_offset,
    #       lsm_gyr_offset)

    # print("The Gyro calibration is done\n")

    # ---------------------------------------------------------------------------- #


def converter(raw_imput, offset_imput, raw_output_lowest, raw_output_highest):
    set_output_lowest = raw_output_lowest - offset_imput
    set_output_highest = raw_output_highest - offset_imput

    set_output_range = raw_output_highest - raw_output_lowest

    if set_output_lowest + offset_imput * 2 < raw_imput and set_output_highest + offset_imput * 2 > raw_imput:
        return (((set_output_highest - set_output_lowest) / set_output_range) * (set_output_range - (raw_output_highest - raw_imput))) + set_output_lowest

    elif set_output_lowest + offset_imput * 2 <= raw_imput and set_output_highest + offset_imput * 2 <= raw_imput:
        return set_output_lowest - (raw_output_highest - raw_imput)
    else:
        return set_output_highest + (raw_output_highest + raw_imput)


def set_roll_pitch_offset(start_offset=10000, offset_steps=1000):
    global prev_time
    global mpu_quats
    # global lsm_quats
    global temp_mpu_roll
    global temp_mpu_pitch
    # global temp_lsm_roll
    # global temp_lsm_pitch

    # ---------------------------- Roll Pitch Offsets ---------------------------- #
    # --------------------------- Calculate Delta Time --------------------------- #
    for roll_pitch_loop in range(start_offset + offset_steps):

        delta_time, prev_time = delta_time_calculate(prev_time)

        # ------------------------------------------------------------------------ #
        # ---------- Read raw measurements from the mpu9250 and lsm9ds1 ---------- #

        acc_mpu, gyr_mpu, tem_mpu = sensor_read(mpu9250)
        # acc_lsm, gyr_lsm, tem_lsm = sensor_read(lsm9ds1)

        mpu_quats = imu_update(acc_mpu, gyr_mpu,  delta_time, mpu_gyr_offset, mpu_quats)
        # lsm_quats = imu_update(acc_lsm, gyr_lsm,  delta_time, lsm_gyr_offset, lsm_quats)

        mpu_roll, mpu_pitch = get_euler(mpu_quats)
        # lsm_roll, lsm_pitch = get_euler(lsm_quats)

        if roll_pitch_loop >= start_offset:
            temp_mpu_roll += mpu_roll / offset_steps
            temp_mpu_pitch += mpu_pitch / offset_steps
            # temp_lsm_roll += lsm_roll / offset_steps
            # temp_lsm_pitch += lsm_pitch / offset_steps

        led_loop("Black", "Green", offset_steps)


def main_loope():
    global prev_time
    global dtsumm
    global mpu_quats
    # global lsm_quats
    global temp_mpu_roll
    global temp_mpu_pitch
    # global temp_lsm_roll
    # global temp_lsm_pitch

    # -------------------------------- Main Loope -------------------------------- #
    # --------------------------- Calculate Delta Time --------------------------- #

    delta_time, prev_time = delta_time_calculate(prev_time)

    # ---------------------------------------------------------------------------- #
    # ------------ Read raw measurements from the mpu9250 and lsm9ds1 ------------ #

    acc_mpu, gyr_mpu, tem_mpu = sensor_read(mpu9250)
    # acc_lsm, gyr_lsm, tem_lsm = sensor_read(lsm9ds1)

    # print(acc_mpu, gyr_mpu, tem_mpu,
    #       acc_lsm, gyr_lsm, tem_lsm)

    mpu_quats = imu_update(acc_mpu, gyr_mpu,  delta_time, mpu_gyr_offset, mpu_quats)
    # lsm_quats = imu_update(acc_lsm, gyr_lsm,  delta_time, lsm_gyr_offset, lsm_quats)

    mpu_roll, mpu_pitch = get_euler(mpu_quats)
    # lsm_roll, lsm_pitch = get_euler(lsm_quats)

    dtsumm += delta_time
    if dtsumm > 0.05:

        # Console output
        # print("ROLL: %-26s" % round(converter(mpu_roll, temp_mpu_roll, -90, 90), 2),
        #       "PITCH: %-26s" % round(converter(mpu_pitch, temp_mpu_pitch, -180, 180), 2),
        #       "TEMP: %-26s" % round(tem_mpu, 2),
        #       "PERIOD %-26s" % delta_time,
        #       "RATE %-26s \n" % int(1 / delta_time))
        print(
            "quatW %-26s" % mpu_quats[0],
            "quatI %-26s" % mpu_quats[1],
            "quatJ %-26s" % mpu_quats[2],
            "quatK %-26s" % mpu_quats[3])

        # print("ROLL: %-26s" % round(converter(lsm_roll, temp_lsm_roll, -90, 90), 2),
        #       "PITCH: %-26s" % round(converter(lsm_pitch, temp_lsm_pitch, -180, 180), 2),
        #       "TEMP: %-26s" % round(tem_lsm, 2),
        #       "PERIOD %-26s" % delta_time,
        #       "RATE %-26s \n" % int(1 / delta_time))

        dtsumm = 0

    led_loop("Black", "Cyan", 250)


if __name__ == '__main__':
    offset_setup()
    set_roll_pitch_offset()
    while True:
        main_loope()
