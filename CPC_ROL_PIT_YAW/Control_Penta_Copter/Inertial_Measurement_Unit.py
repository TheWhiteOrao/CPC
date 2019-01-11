
# imput: sensor read MPU9250 accelerometer_data, gyroscope_data
# output: roll and pitch not converted in a dictionary. like this {roll:deg, pitch:deg}

from datetime import datetime
from math import atan2, sqrt
from cmath import asin, cos

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.07  # 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA = 0.4  # 0.40      # Complementary filter constant


# Kalman filter variables
Q_angle = 0.02
Q_gyro = 0.0015
R_angle = 0.005
y_bias = 0.0
x_bias = 0.0
XP_00 = 0.0
XP_01 = 0.0
XP_10 = 0.0
XP_11 = 0.0
YP_00 = 0.0
YP_01 = 0.0
YP_10 = 0.0
YP_11 = 0.0
KFangleX = 0.0
KFangleY = 0.0


def kalmanFilterY(accAngle, gyroRate, DT):
    y = 0.0
    S = 0.0

    global KFangleY
    global Q_angle
    global Q_gyro
    global y_bias
    global YP_00
    global YP_01
    global YP_10
    global YP_11

    KFangleY = KFangleY + DT * (gyroRate - y_bias)

    YP_00 = YP_00 + (- DT * (YP_10 + YP_01) + Q_angle * DT)
    YP_01 = YP_01 + (- DT * YP_11)
    YP_10 = YP_10 + (- DT * YP_11)
    YP_11 = YP_11 + (+ Q_gyro * DT)

    y = accAngle - KFangleY
    S = YP_00 + R_angle
    K_0 = YP_00 / S
    K_1 = YP_10 / S

    KFangleY = KFangleY + (K_0 * y)
    y_bias = y_bias + (K_1 * y)

    YP_00 = YP_00 - (K_0 * YP_00)
    YP_01 = YP_01 - (K_0 * YP_01)
    YP_10 = YP_10 - (K_1 * YP_00)
    YP_11 = YP_11 - (K_1 * YP_01)

    return KFangleY


def kalmanFilterX(accAngle, gyroRate, DT):
    x = 0.0
    S = 0.0

    global KFangleX
    global Q_angle
    global Q_gyro
    global x_bias
    global XP_00
    global XP_01
    global XP_10
    global XP_11

    KFangleX = KFangleX + DT * (gyroRate - x_bias)

    XP_00 = XP_00 + (- DT * (XP_10 + XP_01) + Q_angle * DT)
    XP_01 = XP_01 + (- DT * XP_11)
    XP_10 = XP_10 + (- DT * XP_11)
    XP_11 = XP_11 + (+ Q_gyro * DT)

    x = accAngle - KFangleX
    S = XP_00 + R_angle
    K_0 = XP_00 / S
    K_1 = XP_10 / S

    KFangleX = KFangleX + (K_0 * x)
    x_bias = x_bias + (K_1 * x)

    XP_00 = XP_00 - (K_0 * XP_00)
    XP_01 = XP_01 - (K_0 * XP_01)
    XP_10 = XP_10 - (K_1 * XP_00)
    XP_11 = XP_11 - (K_1 * XP_01)

    return KFangleX


gyroXangle = 0.0
gyroYangle = 0.0
gyroZangle = 0.0
CFangleX = 0.0
CFangleY = 0.0
kalmanX = 0.0
kalmanY = 0.0

a = datetime.now()


def inertial_measurement_unit(sensor_data):

    global RAD_TO_DEG
    global M_PI
    global G_GAIN
    global AA
    global gyroXangle
    global gyroYangle
    global gyroZangle
    global CFangleX
    global CFangleY
    global a
    global kalmanX
    global kalmanY

    # Read the accelerometer and gyroscope values
    ACCx = sensor_data["acce"]["ax"]
    ACCy = sensor_data["acce"]["ay"]
    ACCz = sensor_data["acce"]["az"]
    GYRx = sensor_data["gyro"]["gx"]
    GYRy = sensor_data["gyro"]["gy"]
    GYRz = sensor_data["gyro"]["gz"]

    # Calculate loop Period(LP). How long between Gyro Reads
    b = datetime.now() - a
    a = datetime.now()
    LP = b.microseconds / (1000000 * 1.0)

    # Convert Gyro raw to degrees per second
    rate_gyr_x = GYRx * G_GAIN
    rate_gyr_y = GYRy * G_GAIN
    rate_gyr_z = GYRz * G_GAIN

    # Calculate the angles from the gyro.
    gyroXangle += rate_gyr_x * LP
    gyroYangle += rate_gyr_y * LP
    gyroZangle += rate_gyr_z * LP

    # Convert Accelerometer values to degrees
    AccXangle = (atan2(ACCy, ACCz) * RAD_TO_DEG)
    AccYangle = (atan2(ACCz, ACCx) + M_PI) * RAD_TO_DEG

    # convert the values to -180 and +180
    if AccYangle > 90:
        AccYangle -= 270.0
    else:
        AccYangle += 90.0

    # Complementary filter used to combine the accelerometer and gyro values.
    CFangleX = AA * (CFangleX + rate_gyr_x * LP) + (1 - AA) * AccXangle
    CFangleY = AA * (CFangleY + rate_gyr_y * LP) + (1 - AA) * AccYangle

    # Kalman filter used to combine the accelerometer and gyro values.
    kalmanY = kalmanFilterY(AccYangle, rate_gyr_y, LP)
    kalmanX = kalmanFilterX(AccXangle, rate_gyr_x, LP)

    # Normalize accelerometer raw values.
    accXnorm = ACCx / sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)
    accYnorm = ACCy / sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)

    # Calculate pitch and roll
    pitch = asin(accXnorm)
    roll = -asin(accYnorm / cos(pitch))

    return pitch, roll, accXnorm, accYnorm, AccXangle, AccYangle, gyroXangle, gyroYangle, gyroZangle, CFangleX, CFangleY, kalmanY, kalmanX
    # print("ax: %-26s" % sensor_data["acce"]["ax"],
    #       "ay: %-26s" % sensor_data["acce"]["ay"],
    #       "az: %-26s" % sensor_data["acce"]["az"],
    #       "gx: %-26s" % sensor_data["gyro"]["gx"],
    #       "gy: %-26s" % sensor_data["gyro"]["gy"],
    #       "gz: %-26s" % sensor_data["gyro"]["gz"],
    #       "te: %-26s" % sensor_data["temp"])


if __name__ == '__main__':
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read

    sensor = sensor_initialize("mpu9250")

    while True:
        IMU = inertial_measurement_unit(sensor_read(sensor))
        print("pitch: %-15s" % round(IMU[0].real, 3),
              "roll: %-15s" % round(IMU[1].real, 3),
              "accXnorm: %-15s" % round(IMU[2], 3),
              "accYnorm: %-15s" % round(IMU[3], 3),
              "AccXangle: %-15s" % round(IMU[4], 3),
              "AccYangle: %-15s" % round(IMU[5], 3),
              "gyroXangle: %-15s" % round(IMU[6], 3),
              "gyroYangle: %-15s" % round(IMU[7], 3),
              "gyroZangle: %-15s" % round(IMU[8], 3),
              "CFangleX: %-15s" % round(IMU[9], 3),
              "CFangleY: %-15s" % round(IMU[10], 3),
              "kalmanY: %-15s" % round(IMU[11], 3),
              "kalmanX: %-15s" % round(IMU[12], 3))
