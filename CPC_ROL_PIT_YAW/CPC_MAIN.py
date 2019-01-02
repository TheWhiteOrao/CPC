from time import *
from CPC_NA2.mpu9250 import *
from CPC_NA2.lsm9ds1 import *
from CPC_SENSORS_READ import sensor_read
from CPC_GYRO_CALI import gyroscope_calibration
from CPC_DELTA_TIME import delta_time_calculate
from CPC_IMU_UPDATA import imu_update

mpu9250 = MPU9250()
lsm9ds1 = LSM9DS1()

mpu_gyr_offset_x = 0
mpu_gyr_offset_y = 0
mpu_gyr_offset_z = 0
lsm_gyr_offset_x = 0
lsm_gyr_offset_y = 0
lsm_gyr_offset_z = 0

mpu_gyr_offset = 0
lsm_gyr_offset = 0


def offset_setup():
    global mpu_gyr_offset_x
    global mpu_gyr_offset_y
    global mpu_gyr_offset_z
    global sm_gyr_offset_x
    global sm_gyr_offset_y
    global sm_gyr_offset_z
    global mpu_gyr_offset
    global lsm_gyr_offset

    # ---------------------------- Sensors Initialize ---------------------------- #

    print("Initialize of mpu9250 and lsm9ds1 sensors starts.")

    mpu9250.initialize()
    lsm9ds1.initialize()

    print("Initialize of mpu9250 and lsm9ds1 sensors is done.\n")

    # ---------------------------------------------------------------------------- #
    # ----------------------------- Gyro Calibration ----------------------------- #

    print("Calibration the Gyro.")

    mpu_gyr_offset = gyroscope_calibration(mpu9250)
    lsm_gyr_offset = gyroscope_calibration(lsm9ds1)

    print("The Gyro calibration is done\n")

    # ---------------------------------------------------------------------------- #


prev_time = 0
dtsumm = 0

mpu_quats = [1, 0, 0, 0,
             1, 0, 0, 0]

lsm_quats = [1, 0, 0, 0,
             1, 0, 0, 0]


def main_loope():
    global prev_time
    global dtsumm
    global mpu_quats
    global lsm_quats

    # -------------------------------- Main Loope -------------------------------- #
    # --------------------------- Calculate Delta Time --------------------------- #

    delta_time, prev_time = delta_time_calculate(prev_time)

    # ---------------------------------------------------------------------------- #
    # ------------ Read raw measurements from the mpu9250 and lsm9ds1 ------------ #

    acc_mpu, gyr_mpu, mag_mpu, tem_mpu = sensor_read(mpu9250)
    acc_lsm, gyr_lsm, mag_lsm, tem_lsm = sensor_read(lsm9ds1)

    print(acc_mpu, gyr_mpu, mag_mpu, tem_mpu,
          acc_lsm, gyr_lsm, mag_lsm, tem_lsm)

    mpu_quats = imu_update(acc_mpu, gyr_mpu, mag_mpu, delta_time, mpu_gyr_offset, mpu_quats)
    lsm_quats = imu_update(acc_lsm, gyr_lsm, mag_lsm, delta_time, lsm_gyr_offset, lsm_quats)

    mpu_roll, mpu_pitch, mpu_yaw = get_euler(mpu_quats)
    lsm_roll, lsm_pitch, lsm_yaw = get_euler(lsm_quats)

    dtsumm += delta_time
    if dtsumm > 0.05:

        # Console output
        print("ROLL: %-26s" % round(mpu_roll, 2),
              "PITCH: %-26s" % round(mpu_pitch, 2),
              "YAW: %-26s" % round(mpu_yaw * -1, 2),
              "PERIOD %-26s" % delta_time,
              "RATE %-26s \n" % int(1 / delta_time))

        print("ROLL: %-26s" % round(lsm_roll, 2),
              "PITCH: %-26s" % round(lsm_pitch, 2),
              "YAW: %-26s" % round(lsm_yaw * -1, 2),
              "PERIOD %-26s" % delta_time,
              "RATE %-26s \n" % int(1 / delta_time))

        dtsumm = 0


offset_setup()
while True:
    main_loope()
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
