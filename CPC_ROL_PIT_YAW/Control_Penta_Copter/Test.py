
# x = dict(map(lambda x: (x, 0), range(1, 20)))
# print(x)
# h = []
# h.append(1)
# h = {}
# h.

# h = {0: 143, 1: 324634673, 2: 34346, 3: 2332, 4: 235, 5: 45756, 6: 325, 7: 12421, 8: 4211223, 9: 12342311, 10: 8786, 11: 345}
# l = {}
# for i in range(len(h)):
#     l[i] = (h[i] * 2 / 3463)**-0.5
# print(l)
# k1 = (h[0] * 2 / 3463)**-0.5
# k2 = (h[1] * 2 / 3463)**-0.5
# k3 = (h[2] * 2 / 3463)**-0.5
# k4 = (h[3] * 2 / 3463)**-0.5
# k5 = (h[4] * 2 / 3463)**-0.5
# k6 = (h[5] * 2 / 3463)**-0.5
# k7 = (h[6] * 2 / 3463)**-0.5
# k8 = (h[7] * 2 / 3463)**-0.5
# k9 = (h[8] * 2 / 3463)**-0.5
# k10 = (h[9] * 2 / 3463)**-0.5
# k11 = (h[10] * 2 / 3463)**-0.5
# k12 = (h[11] * 2 / 3463)**-0.5
#
#
# print(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12)

# h = {0: 1, 1: 19}
#
# for i in h:
#     print(h[i])

# from Receiver_Input import receiver_imput
# from Receiver_Signal_Converter import receiver_signal_converter
# from time import process_time_ns
#
# h = 0
# while True:
#     # receiver_signal_converter(receiver_imput({0: (0, 1), 1: (-1, 1), 2: (-1, 1), 3: (-1, 1)}))
#     print(1000000000 / (process_time_ns() - h))
#     h = process_time_ns()

#
# h = {1: 0}
#
# if h == dict():
#     print("emty")
# elif type(h) == dict:
#     print("full")
# else:
#     print("rong type")
#!/usr/bin/python
#	This is the base code needed to get usable angles from a BerryIMU
#	using a Complementary filter. The readings can be improved by
#	adding more filters, E.g Kalman, Low pass, median filter, etc..
#   See berryIMU.py for more advanced code.
#
#	For this code to work correctly, BerryIMU must be facing the
#	correct way up. This is when the Skull Logo on the PCB is facing down.
#
#   Both the BerryIMUv1 and BerryIMUv2 are supported
#
#	http://ozzmaker.com/


import time
import math
import IMU
import datetime
import os


RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA = 0.40      # Complementary filter constant

################# Compass Calibration values ############
# Use calibrateBerryIMU.py to get calibration values
# Calibrating the compass isnt mandatory, however a calibrated
# compass will result in a more accurate heading values.


gyroXangle = 0.0
gyroYangle = 0.0
gyroZangle = 0.0
CFangleX = 0.0
CFangleY = 0.0


IMU.detectIMU()  # Detect if BerryIMUv1 or BerryIMUv2 is connected.
IMU.initIMU()  # Initialise the accelerometer, gyroscope and compass


a = datetime.datetime.now()


while True:

    # Read the accelerometer,gyroscope values
    ACCx = IMU.readACCx()
    ACCy = IMU.readACCy()
    ACCz = IMU.readACCz()
    GYRx = IMU.readGYRx()
    GYRy = IMU.readGYRy()
    GYRz = IMU.readGYRz()

    # Calculate loop Period(LP). How long between Gyro Reads
    b = datetime.datetime.now() - a
    a = datetime.datetime.now()
    LP = b.microseconds / (1000000 * 1.0)
    print "Loop Time | %5.2f|" % (LP),

    # Convert Gyro raw to degrees per second
    rate_gyr_x = GYRx * G_GAIN
    rate_gyr_y = GYRy * G_GAIN
    rate_gyr_z = GYRz * G_GAIN

    # Calculate the angles from the gyro.
    gyroXangle += rate_gyr_x * LP
    gyroYangle += rate_gyr_y * LP
    gyroZangle += rate_gyr_z * LP

    # Convert Accelerometer values to degrees
    AccXangle = (math.atan2(ACCy, ACCz) * RAD_TO_DEG)
    AccYangle = (math.atan2(ACCz, ACCx) + M_PI) * RAD_TO_DEG

    # convert the values to -180 and +180
    if AccYangle > 90:
        AccYangle -= 270.0
    else:
        AccYangle += 90.0

    # Complementary filter used to combine the accelerometer and gyro values.
    CFangleX = AA * (CFangleX + rate_gyr_x * LP) + (1 - AA) * AccXangle
    CFangleY = AA * (CFangleY + rate_gyr_y * LP) + (1 - AA) * AccYangle

    # Normalize accelerometer raw values.
    accXnorm = ACCx / math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)
    accYnorm = ACCy / math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)

    # Calculate pitch and roll
    pitch = math.asin(accXnorm)
    roll = -math.asin(accYnorm / math.cos(pitch))

    # slow program down a bit, makes the output more readable
    time.sleep(0.03)
