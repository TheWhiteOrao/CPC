# -------------------------------------------------------------------------------------------------- #
#   Quaternionen-Algebra:                            ││             ·  │  1  │  i  │  j  │  k  │     #
#   ───────────────────────                          ││             ───┼─────┼─────┼─────┼─────┼─    #
#   i² = j² = k² = ijk = -1                          ││             1  │  1  │  i  │  j  │  k  │     #
#                                                    ││             ───┼─────┼─────┼─────┼─────┼─    #
#   Multiplication of i, j, k not commutative:       ││             i  │  i  │ - 1 │  k  │ - j │     #
#   ij ≠ ji                                          ││             ───┼─────┼─────┼─────┼─────┼─    #
#                                                    ││             j  │  j  │ - k │ - 1 │  i  │     #
#   i² = -1    j² = -1    k² = -1                    ││             ───┼─────┼─────┼─────┼─────┼─    #
#   ij =  k    ji = -k    ki =  j                    ││             k  │  k  │  j  │ - i │ - 1 │     #
#   ik = -j    jk =  i    kj = -i                    ││             ───┼─────┼─────┼─────┼─────┼─    #
#                                                    ││                                              #
# -------------------------------------------------------------------------------------------------- #

# -------------------------------------- Original Code in C++ -------------------------------------- #
#                                                                                                    #
#                          Written by Igor Vereninov and Mikhail Avkhimenia                          #
#                      twitter.com/emlidtech || www.emlid.com || info@emlid.com                      #
#                                                                                                    #
# -------------------------------------------------------------------------------------------------- #

# -------------------------------------------------------------------------------------------------- #
#                                                                                                    #
#                            Radio Control Stabiliser Quaternion Based python                        #
#                                             by S1897                                               #
#                                                                                                    #
# -------------------------------------------------------------------------------------------------- #

# ------------------- Output format of the function sensor_read("sensor_name") --------------------- #
#                               {                                                                    #
#                               "acce": {"acceX": x, "acceY": y, "acceZ": z},                                 #
#                               "gyro": {"gyroX": x, "gyroY": y, "gyroZ": z},                                 #
#                               "magn": {"magnX": x, "magnY": y, "magnZ": z},                                 #
#                               "temp": C°                                                           #
#                               }                                                                    #
# -------------------------------------------------------------------------------------------------- #

# ------------------------------------ Global system variables ------------------------------------- #

QuatDirc = {"QuatW": 0.0, "QuatX": 0.0, "QuatY": 0.0, "QuatZ": 1.0}                                  # estimated orientation quaternion elements with initial conditions

PI = 3.14159
GR = 9.80665

twoKi = 0
twoKp = 2

# --------------------------------------------------- AGM Inertial measurement unit --------------------------------------------------- #


def RCSQB_AGM(sensor_output, deltat, gyroCaliOffset):

    global PI, GR, QuatDirc, twoKi, twoKp

    # Accelerometer measurements
    acceX = sensor_output["acce"]["ax"]
    acceY = sensor_output["acce"]["ay"]
    acceZ = sensor_output["acce"]["az"]

    # Gyroscope measurements in rad/s
    gyroX = sensor_output["gyro"]["gx"]
    gyroY = sensor_output["gyro"]["gy"]
    gyroZ = sensor_output["gyro"]["gz"]

    # Magnetometer measurements
    magnX = sensor_output["magn"]["mx"]
    magnY = sensor_output["magn"]["my"]
    magnZ = sensor_output["magn"]["mz"]

    # Set quaternion to local variables
    QuatW = QuatDirc["QuatW"]
    QuatX = QuatDirc["QuatX"]
    QuatY = QuatDirc["QuatY"]
    QuatZ = QuatDirc["QuatZ"]

    # Use IMU algorithm if magnetometer measurement invalid(avoids NaN in magnetometer normalisation)
    if (magnX == 0.0) and (magnY == 0.0) and (magnZ == 0.0):
        return RCSQB_AG(sensor_output, deltat, gyroCaliOffset)

    # Compute feedback only if accelerometer measurement valid(avoids NaN in accelerometer normalisation)
    if not ((acceX == 0.0) and (acceY == 0.0) and (acceZ == 0.0)):

        # Normalise accelerometer measurement
        acceNorm = (acceX * acceX + acceY * acceY + acceZ * acceZ) ** 0.5
        acceX /= acceNorm
        acceY /= acceNorm
        acceZ /= acceNorm

        # Normalise magnetometer measurement
        magnNorm = (magnX * magnX + magnY * magnY + magnZ * magnZ) ** 0.5
        magnX /= magnNorm
        magnY /= magnNorm
        magnZ /= magnNorm

        # Auxiliary variables to avoid repeated arithmetic
        QuatWQuatW = QuatW * QuatW
        QuatWQuatX = QuatW * QuatX
        QuatWQuatY = QuatW * QuatY
        QuatWQuatZ = QuatW * QuatZ
        QuatXQuatX = QuatX * QuatX
        QuatXQuatY = QuatX * QuatY
        QuatXQuatZ = QuatX * QuatZ
        QuatYQuatY = QuatY * QuatY
        QuatYQuatZ = QuatY * QuatZ
        QuatZQuatZ = QuatZ * QuatZ

        # Reference direction of Earth's magnetic field
        hx = 2.0 * (magnX * (0.5 - QuatYQuatY - QuatZQuatZ) + magnY * (QuatXQuatY - QuatWQuatZ) + magnZ * (QuatXQuatZ + QuatWQuatY))
        hy = 2.0 * (magnX * (QuatXQuatY + QuatWQuatZ) + magnY * (0.5 - QuatXQuatX - QuatZQuatZ) + magnZ * (QuatYQuatZ - QuatWQuatX))
        bx = (hx * hx + hy * hy) ** 0.5
        bz = 2.0 * (magnX * (QuatXQuatZ - QuatWQuatY) + magnY * (QuatYQuatZ + QuatWQuatX) + magnZ * (0.5 - QuatXQuatX - QuatYQuatY))

        # Estimated direction of gravity and magnetic field
        halfvx = QuatXQuatZ - QuatWQuatY
        halfvy = QuatWQuatX + QuatYQuatZ
        halfvz = QuatWQuatW - 0.5 + QuatZQuatZ
        halfwx = bx * (0.5 - QuatYQuatY - QuatZQuatZ) + bz * (QuatXQuatZ - QuatWQuatY)
        halfwy = bx * (QuatXQuatY - QuatWQuatZ) + bz * (QuatWQuatX + QuatYQuatZ)
        halfwz = bx * (QuatWQuatY + QuatXQuatZ) + bz * (0.5 - QuatXQuatX - QuatYQuatY)

        # Error is sum of cross product between estimated direction and measured direction of field vectors
        halfex = (acceY * halfvz - acceZ * halfvy) + (magnY * halfwz - magnZ * halfwy)
        halfey = (acceZ * halfvx - acceX * halfvz) + (magnZ * halfwx - magnX * halfwz)
        halfez = (acceX * halfvy - acceY * halfvx) + (magnX * halfwy - magnY * halfwx)

        # Compute and apply integral feedback if enabled
        if twoKi > 0.0:

            # integral error scaled by Ki
            integralFBx += twoKi * halfex * deltat
            integralFBy += twoKi * halfey * deltat
            integralFBz += twoKi * halfez * deltat

            # apply integral feedback
            gyroX += integralFBx
            gyroY += integralFBy
            gyroZ += integralFBz

        else:

            # prevent integral windup
            integralFBx = 0.0
            integralFBy = 0.0
            integralFBz = 0.0

        # Apply proportional feedback
        gyroX += twoKp * halfex
        gyroY += twoKp * halfey
        gyroZ += twoKp * halfez

    # Integrate rate of change of quaternion
    # pre - multiply common factors
    gyroX *= (0.5 * deltat)
    gyroY *= (0.5 * deltat)
    gyroZ *= (0.5 * deltat)
    QuatA = QuatW
    QuatB = QuatX
    QuatC = QuatY
    QuatW += (-QuatB * gyroX - QuatC * gyroY - QuatZ * gyroZ)
    QuatX += (QuatA * gyroX + QuatC * gyroZ - QuatZ * gyroY)
    QuatY += (QuatA * gyroY - QuatB * gyroZ + QuatZ * gyroX)
    QuatZ += (QuatA * gyroZ + QuatB * gyroY - QuatC * gyroX)

    # Normalise quaternion
    QuatNorm = (QuatW * QuatW + QuatX * QuatX + QuatY * QuatY + QuatZ * QuatZ) ** 0.5
    QuatW /= QuatNorm
    QuatX /= QuatNorm
    QuatY /= QuatNorm
    QuatZ /= QuatNorm

    # Set QuatDirc
    QuatDirc["QuatW"] = QuatW
    QuatDirc["QuatX"] = QuatX
    QuatDirc["QuatY"] = QuatY
    QuatDirc["QuatZ"] = QuatZ

    return QuatDirc


def RCSQB_AG(sensor_output, deltat):

    global PI, GR, QuatDirc

    # Accelerometer measurements
    acceX = sensor_output["acce"]["ax"]
    acceY = sensor_output["acce"]["ay"]
    acceZ = sensor_output["acce"]["az"]

    # Gyroscope measurements in rad/s
    gyroX = sensor_output["gyro"]["gx"]
    gyroY = sensor_output["gyro"]["gy"]
    gyroZ = sensor_output["gyro"]["gz"]

    # Set quaternion to local variables
    QuatW = QuatDirc["QuatW"]
    QuatX = QuatDirc["QuatX"]
    QuatY = QuatDirc["QuatY"]
    QuatZ = QuatDirc["QuatZ"]

    acceX /= GR
    acceY /= GR
    acceZ /= GR

    gyroX *= (180 / PI) * 0.0175
    gyroY *= (180 / PI) * 0.0175
    gyroZ *= (180 / PI) * 0.0175

    gyroX -= gyroCaliOffset["gx"]
    gyroY -= gyroCaliOffset["gy"]
    gyroZ -= gyroCaliOffset["gz"]

    # Compute feedback only if accelerometer measurement valid(avoids NaN in accelerometer normalisation)
    if not ((acceX == 0.0) and (acceY == 0.0) and (acceZ == 0.0)):

        # Normalise accelerometer measurement
        acceNorm = (acceX * acceX + acceY * acceY + acceZ * acceZ) ** 0.5
        acceX /= acceNorm
        acceY /= acceNorm
        acceZ /= acceNorm

        # Estimated direction of gravity and vector perpendicular to magnetic flux
        halfvx = QuatX * QuatZ - QuatW * QuatY
        halfvy = QuatW * QuatX + QuatY * QuatZ
        halfvz = QuatW * QuatW - 0.5 + QuatZ * QuatZ

        # Error is sum of cross product between estimated and measured direction of gravity
        halfex = (acceY * halfvz - acceZ * halfvy)
        halfey = (acceZ * halfvx - acceX * halfvz)
        halfez = (acceX * halfvy - acceY * halfvx)

        # Compute and apply integral feedback if enabled
        if twoKi > 0.0:

            # integral error scaled by Ki
            integralFBx += twoKi * halfex * deltat
            integralFBy += twoKi * halfey * deltat
            integralFBz += twoKi * halfez * deltat

            # apply integral feedback
            gyroX += integralFBx
            gyroY += integralFBy
            gyroZ += integralFBz

        else:

            # prevent integral windup
            integralFBx = 0.0
            integralFBy = 0.0
            integralFBz = 0.0

        # Apply proportional feedback
        gyroX += twoKp * halfex
        gyroY += twoKp * halfey
        gyroZ += twoKp * halfez

    # Integrate rate of change of quaternion
    # pre - multiply common factors
    gyroX *= (0.5 * deltat)
    gyroY *= (0.5 * deltat)
    gyroZ *= (0.5 * deltat)
    QuatA = QuatW
    QuatB = QuatX
    QuatC = QuatY
    QuatW += (-QuatB * gyroX - QuatC * gyroY - QuatZ * gyroZ)
    QuatX += (QuatA * gyroX + QuatC * gyroZ - QuatZ * gyroY)
    QuatY += (QuatA * gyroY - QuatB * gyroZ + QuatZ * gyroX)
    QuatZ += (QuatA * gyroZ + QuatB * gyroY - QuatC * gyroX)

    # Normalise quaternion
    QuatNorm = (QuatW * QuatW + QuatX * QuatX + QuatY * QuatY + QuatZ * QuatZ) ** 0.5
    QuatW /= QuatNorm
    QuatX /= QuatNorm
    QuatY /= QuatNorm
    QuatZ /= QuatNorm

    # Set QuatDirc
    QuatDirc["QuatW"] = QuatW
    QuatDirc["QuatX"] = QuatX
    QuatDirc["QuatY"] = QuatY
    QuatDirc["QuatZ"] = QuatZ

    return QuatDirc
#
# def getEuler(float * roll, float * pitch, float * yaw)
#
#     roll = atan2(2 * (QuatW * QuatX + QuatY * QuatZ), 1 - 2 * (QuatX * QuatX + QuatY * QuatY)) * 180.0 / M_PI
#     pitch = asin(2 * (QuatW * QuatY - QuatZ * QuatX)) * 180.0 / M_PI
#     yaw = atan2(2 * (QuatW * QuatZ + QuatX * QuatY), 1 - 2 * (QuatY * QuatY + QuatZ * QuatZ)) * 180.0 / M_PI


if __name__ == '__main__':
    from time import sleep
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read
    from Delta_Time import calculate_delta_time
    from Gyrometer_Calibration import gyroscope_calibration

    sensor = sensor_initialize("lsm9ds1")

    gyroOffset = gyroscope_calibration(sensor, 1000)

    delta_time, Hz, current_delta_time = calculate_delta_time()

    while True:

        delta_time, Hz, current_delta_time = calculate_delta_time(current_delta_time, Hz)

        p = RCSQB_AGM(sensor_read(sensor), delta_time, gyroOffset)
        sleep(0.001)

        print("QuatW: %-15s" % round(p["QuatW"], 3),
              "QuatX: %-15s" % round(p["QuatX"], 3),
              "QuatY: %-15s" % round(p["QuatY"], 3),
              "QuatZ: %-15s" % round(p["QuatZ"], 3),
              "Hz: %-15s" % round(Hz, 3),
              )
