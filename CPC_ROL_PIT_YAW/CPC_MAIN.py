from time import *
from CPC_NA2.mpu9250 import *
from CPC_NA2.lsm9ds1 import *
from CPC_SENSORS_READ import sensor_read
from CPC_GYRO_CALI import gyroscope_calibration
from CPC_DELTA_TIME import delta_time_calculate
from CPC_IMU_UPDATA import *

mpu9250 = MPU9250()
lsm9ds1 = LSM9DS1()

mpu_gyr_offset = 0
lsm_gyr_offset = 0


def offset_setup():
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

    print(mpu_gyr_offset,
          lsm_gyr_offset)

    print("The Gyro calibration is done\n")

    sleep(2)

    # ---------------------------------------------------------------------------- #


prev_time = 0
dtsumm = 0

I = 0
r_mup = 1
r_lsm = 1
p_mup = 1
p_lsm = 1

mpu_quats = [1, 0, 0, 0,
             1, 0, 0, 0]

lsm_quats = [1, 0, 0, 0,
             1, 0, 0, 0]

pi = 3.14159265358


def main_loope():
    global I
    global r_mup
    global r_lsm
    global p_mup
    global p_lsm
    global pi

    global prev_time
    global dtsumm
    global mpu_quats
    global lsm_quats

    # -------------------------------- Main Loope -------------------------------- #
    # --------------------------- Calculate Delta Time --------------------------- #

    delta_time, prev_time = delta_time_calculate(prev_time)

    # ---------------------------------------------------------------------------- #
    # ------------ Read raw measurements from the mpu9250 and lsm9ds1 ------------ #

    acc_mpu, gyr_mpu, tem_mpu = sensor_read(mpu9250)
    acc_lsm, gyr_lsm, tem_lsm = sensor_read(lsm9ds1)

    # print(acc_mpu, gyr_mpu, tem_mpu,
    #       acc_lsm, gyr_lsm, tem_lsm)

    mpu_quats = imu_update(acc_mpu, gyr_mpu,  delta_time, mpu_gyr_offset, mpu_quats)
    lsm_quats = imu_update(acc_lsm, gyr_lsm,  delta_time, lsm_gyr_offset, lsm_quats)

    mpu_roll, mpu_pitch = get_euler(mpu_quats, r_mup * pi / 180, p_mup * pi / 180)
    lsm_roll, lsm_pitch = get_euler(lsm_quats, r_lsm * pi / 180, p_lsm * pi / 180)

    if I > 10000 and I <= 11000:
        if I == 10001:
            r_mup -= 1
            r_lsm -= 1
            p_mup -= 1
            p_lsm -= 1

        r_mup += mpu_roll / 1000
        r_lsm += lsm_roll / 1000
        p_mup += mpu_pitch / 1000
        p_lsm += lsm_pitch / 1000

    dtsumm += delta_time
    if dtsumm > 0.05:

        # Console output
        print("ROLL: %-26s" % round(mpu_roll - r_mup, 2),
              "PITCH: %-26s" % round(mpu_pitch - p_mup, 2),
              "TEMP: %-26s" % round(tem_mpu, 2),
              "PERIOD %-26s" % delta_time,
              "RATE %-26s \n" % int(1 / delta_time))

        print("ROLL: %-26s" % round(lsm_roll - r_lsm, 2),
              "PITCH: %-26s" % round(lsm_pitch - p_lsm, 2),
              "TEMP: %-26s" % round(tem_lsm, 2),
              "PERIOD %-26s" % delta_time,
              "RATE %-26s \n" % int(1 / delta_time))

        dtsumm = 0

    I += 1


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
