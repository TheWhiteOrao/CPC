
# imput: sensor read MPU9250 accelerometer_data, gyroscope_data
# output: roll and pitch not converted in a dictionary. like this {roll:deg, pitch:deg}

from datetime import datetime
from math import atan2, sqrt, asin, cos

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA = 0.40      # Complementary filter constant

gyroXangle = 0.0
gyroYangle = 0.0
gyroZangle = 0.0
CFangleX = 0.0
CFangleY = 0.0

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

    return pitch, roll
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
        print(IMU)
