from time import *
from CPC_NA2.mpu9250 import *
from CPC_NA2.lsm9ds1 import *
from CPC_SENSORS_READ import sensor_read
from CPC_GYRO_CALI import gyroscope_calibration
from CPC_DELTA_TIME import delta_time_calculate


mpu9250 = MPU9250()
lsm9ds1 = LSM9DS1()


def offset_setup():

    # ---------------------------- Sensors Initialize ---------------------------- #

    print("Initialize of mpu9250 and lsm9ds1 sensors starts.")

    mpu9250.initialize()
    lsm9ds1.initialize()

    print("Initialize of mpu9250 and lsm9ds1 sensors is done.\n")

    # ---------------------------------------------------------------------------- #
    # ----------------------------- Gyro Calibration ----------------------------- #

    print("Calibration the Gyro.")

    mpu_gyr_offset_x, mpu_gyr_offset_y, mpu_gyr_offset_z = gyroscope_calibration(mpu9250)
    lsm_gyr_offset_x, lsm_gyr_offset_y, lsm_gyr_offset_z = gyroscope_calibration(lsm9ds1)

    print("The Gyro calibration is done\n")

    # ---------------------------------------------------------------------------- #


prev_time = 0


def main_loope():
    global prev_time

    # -------------------------------- Main Loope -------------------------------- #
    # --------------------------- Calculate Delta Time --------------------------- #

    delta_time, prev_time = delta_time_calculate(prev_time)

    # ---------------------------------------------------------------------------- #
    # ------------ Read raw measurements from the mpu9250 and lsm9ds1 ------------ #

    acc_mpu, gyr_mpu, mag_mpu, tem_mpu = sensor_read(mpu9250)
    acc_lsm, gyr_lsm, mag_lsm, tem_lsm = sensor_read(lsm9ds1)

    acc_mpu_x = acc_mpu[0]
    acc_mpu_y = acc_mpu[1]
    acc_mpu_z = acc_mpu[2]

    gyr_mpu_x = gyr_mpu[0]
    gyr_mpu_y = gyr_mpu[1]
    gyr_mpu_z = gyr_mpu[2]

    mag_mpu_x = mag_mpu[0]
    mag_mpu_y = mag_mpu[1]
    mag_mpu_z = mag_mpu[2]

    acc_lsm_x = acc_lsm[0]
    acc_lsm_y = acc_lsm[1]
    acc_lsm_z = acc_lsm[2]

    gyr_lsm_x = gyr_lsm[0]
    gyr_lsm_y = gyr_lsm[1]
    gyr_lsm_z = gyr_lsm[2]

    mag_lsm_x = mag_lsm[0]
    mag_lsm_y = mag_lsm[1]
    mag_lsm_z = mag_lsm[2]

    # print("acc_mpu: %-26s" % acc_mpu[0],
    #       "%-26s" % acc_mpu[1],
    #       "%-26s" % acc_mpu[2],
    #       "gyr_mpu: %-26s" % gyr_mpu[0],
    #       "%-26s" % gyr_mpu[1],
    #       "%-26s" % gyr_mpu[2],
    #       "mag_mpu: %-26s" % mag_mpu[0],
    #       "%-26s" % mag_mpu[1],
    #       "%-26s" % mag_mpu[2],
    #       "tem_mpu: %-26s" % tem_mpu
    #       )
    #
    # print("acc_lsm: %-26s" % acc_lsm[0],
    #       "%-26s" % acc_lsm[1],
    #       "%-26s" % acc_lsm[2],
    #       "gyr_lsm: %-26s" % gyr_lsm[0],
    #       "%-26s" % gyr_lsm[1],
    #       "%-26s" % gyr_lsm[2],
    #       "mag_lsm: %-26s" % mag_lsm[0],
    #       "%-26s" % mag_lsm[1],
    #       "%-26s" % mag_lsm[2],
    #       "tem_lsm: %-26s" % tem_lsm
    #       )
