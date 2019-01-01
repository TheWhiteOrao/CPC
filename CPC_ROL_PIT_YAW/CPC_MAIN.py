from time import *
from CPC_NA2.mpu9250 import *
from CPC_NA2.lsm9ds1 import *
from CPC_SENSORS_READ import *


mpu9250 = MPU9250()
lsm9ds1 = LSM9DS1()


def offset_setup():

    # ---------------------------- Sensors Initialize ---------------------------- #

    print("Initialize of mpu9250 and lsm9ds1 sensors starts.\n")

    mpu9250.initialize()
    lsm9ds1.initialize()

    print("Initialize of mpu9250 and lsm9ds1 sensors is done.\n")

    # ---------------------------------------------------------------------------- #

    print("Beginning to calibration the Gyro.\n")


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
