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

# ------------------ IMU filter implementation optimized in C translate to python ------------------ #
#                                                                                                    #
#                         Original source code from the paper described below:                       #
#                                                                                                    #
#         An efficient orientation filter for inertial and inertial/magnetic sensor arrays           #
#                                     by Sebastian O.H. Madgwick                                     #
#                                                                                                    #
# -------------------------------------------------------------------------------------------------- #

# -------------------------------------------------------------------------------------------------- #
#                                                                                                    #
#                            Radio Control Stabiliser Quaternion Based                               #
#                                             by S1897                                               #
#                                                                                                    #
# -------------------------------------------------------------------------------------------------- #

# ------------------- Output format of the function sensor_read("sensor_name") --------------------- #
#                               {                                                                    #
#                               "acce": {"ax": x, "ay": y, "az": z},                                 #
#                               "gyro": {"gx": x, "gy": y, "gz": z},                                 #
#                               "magn": {"mx": x, "my": y, "mz": z},                                 #
#                               "temp": C°                                                           #
#                               }                                                                    #
# -------------------------------------------------------------------------------------------------- #

# ---------------------------------------- System constants ---------------------------------------- #

# deltat = 0.001                                                                                     # sampling period in seconds (shown as 1 ms)
gyroMeasError = 3.14159265358979 * (5.0 / 180.0)                                                     # gyroscope measurement error in rad/s (shown as 5 deg/s)
gyroMeasDrift = 3.14159265358979 * (0.2 / 180.0)                                                     # gyroscope measurement error in rad/s/s (shown as 0.2 deg/s/s)
beta = ((3.0 / 4.0)**5) * gyroMeasError                                                              # compute beta
zeta = ((3.0 / 4.0)**5) * gyroMeasDrift                                                              # compute zeta

b_x, b_z = 1, 0                                                                                      # reference direction of flux in earth frame
w_bx, w_by, w_bz = 0, 0, 0                                                                           # estimate gyroscope biases error


# -------------------------------------------------------------------------------------------------- #

# ------------------------------------ Global system variables ------------------------------------- #

QuatDirc = {"QuatW": 1.0, "QuatX": 0.0, "QuatY": 0.0, "QuatZ": 0.0}                                  # estimated orientation quaternion elements with initial conditions

# -------------------------------------------------------------------------------------------------- #


def RCSQB_AG(sensor_output, deltat):

    # ------------------------------- Global variables in RCSQB_AG --------------------------------- #

    # global deltat
    global gyroMeasError
    global beta
    global QuatDirc                                                                                  # estimated orientation quaternion elements with initial conditions

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------- Binds sensor outputs to multiple variables ------------------------- #

    acceX = sensor_output["acce"]["ax"]
    acceY = sensor_output["acce"]["ay"]
    acceZ = sensor_output["acce"]["az"]

    gyroX = sensor_output["gyro"]["gx"]
    gyroY = sensor_output["gyro"]["gy"]
    gyroZ = sensor_output["gyro"]["gz"]

    # ---------------------------------------------------------------------------------------------- #

    # --------------------- Axulirary variables to avoid reapeated calcualtions --------------------- #

    half_QuatW = 0.5 * QuatDirc["QuatW"]
    half_QuatX = 0.5 * QuatDirc["QuatX"]
    half_QuatY = 0.5 * QuatDirc["QuatY"]
    half_QuatZ = 0.5 * QuatDirc["QuatZ"]

    two_QuatW = 2.0 * QuatDirc["QuatW"]
    two_QuatX = 2.0 * QuatDirc["QuatX"]
    two_QuatY = 2.0 * QuatDirc["QuatY"]
    two_QuatZ = 2.0 * QuatDirc["QuatZ"]

    # ---------------------------------------------------------------------------------------------- #

    # -------------------------- Normalise the accelerometer measurement --------------------------- #

    acceNorm = (acceX * acceX + acceY * acceY + acceZ * acceZ) ** 0.5
    acceX /= acceNorm
    acceY /= acceNorm
    acceZ /= acceNorm

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------ Compute the objective function and Jacobian ------------------------- #

    f_1 = two_QuatX * QuatDirc["QuatZ"] - two_QuatW * QuatDirc["QuatY"] - acceX
    f_2 = two_QuatW * QuatDirc["QuatX"] + two_QuatY * QuatDirc["QuatZ"] - acceY
    f_3 = 1.0 - two_QuatX * QuatDirc["QuatX"] - two_QuatY * QuatDirc["QuatY"] - acceZ

    J_11or24 = two_QuatY                                                                             # J_11 negated in matrix multiplication
    J_12or23 = 2.0 * QuatDirc["QuatZ"]
    J_13or22 = two_QuatW                                                                             # J_12 negated in matrix multiplication
    J_14or21 = two_QuatX
    J_32 = 2.0 * J_14or21                                                                            # negated in matrix multiplication
    J_33 = 2.0 * J_11or24                                                                            # negated in matrix multiplication

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------ Compute the gradient(matrix multiplication) ------------------------- #

    QuatW_HatDot = J_14or21 * f_2 - J_11or24 * f_1
    QuatX_HatDot = J_12or23 * f_1 + J_13or22 * f_2 - J_32 * f_3
    QuatY_HatDot = J_12or23 * f_2 - J_33 * f_3 - J_13or22 * f_1
    QuatZ_HatDot = J_14or21 * f_1 + J_11or24 * f_2

    # ---------------------------------------------------------------------------------------------- #

    # Normalise the gradient

    gradNorm = (QuatW_HatDot * QuatW_HatDot + QuatX_HatDot * QuatX_HatDot + QuatY_HatDot * QuatY_HatDot + QuatZ_HatDot * QuatZ_HatDot) ** 0.5
    QuatW_HatDot /= gradNorm
    QuatX_HatDot /= gradNorm
    QuatY_HatDot /= gradNorm
    QuatZ_HatDot /= gradNorm

    # ---------------------------------------------------------------------------------------------- #

    # Compute the quaternion derrivative measured by gyroscopes

    DotOmegaQuatW = -half_QuatX * gyroX - half_QuatY * gyroY - half_QuatZ * gyroZ
    DotOmegaQuatX = half_QuatW * gyroX + half_QuatY * gyroZ - half_QuatZ * gyroY
    DotOmegaQuatY = half_QuatW * gyroY - half_QuatX * gyroZ + half_QuatZ * gyroX
    DotOmegaQuatZ = half_QuatW * gyroZ + half_QuatX * gyroY - half_QuatY * gyroX

    # ---------------------------------------------------------------------------------------------- #

    # Compute then integrate the estimated quaternion derrivative

    QuatDirc["QuatW"] += (DotOmegaQuatW - (beta * QuatW_HatDot)) * deltat
    QuatDirc["QuatX"] += (DotOmegaQuatX - (beta * QuatX_HatDot)) * deltat
    QuatDirc["QuatY"] += (DotOmegaQuatY - (beta * QuatY_HatDot)) * deltat
    QuatDirc["QuatZ"] += (DotOmegaQuatZ - (beta * QuatZ_HatDot)) * deltat

    # ---------------------------------------------------------------------------------------------- #

    # Normalise quaternion

    quatNorm = (QuatDirc["QuatW"] * QuatDirc["QuatW"] + QuatDirc["QuatX"] * QuatDirc["QuatX"] + QuatDirc["QuatY"] * QuatDirc["QuatY"] + QuatDirc["QuatZ"] * QuatDirc["QuatZ"]) ** 0.5
    QuatDirc["QuatW"] /= quatNorm
    QuatDirc["QuatX"] /= quatNorm
    QuatDirc["QuatY"] /= quatNorm
    QuatDirc["QuatZ"] /= quatNorm

    # ---------------------------------------------------------------------------------------------- #

    return QuatDirc


def RCSQB_AGM(sensor_output, deltat):

    # ------------------------------- Global variables in RCSQB_AG --------------------------------- #

    # global deltat
    global b_x, b_z
    global w_bx, w_by, w_bz
    global gyroMeasError
    global gyroMeasDrift
    global beta
    global zeta
    global QuatDirc                                                                                  # estimated orientation quaternion elements with initial conditions

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------- Binds sensor outputs to multiple variables ------------------------- #

    acceX = sensor_output["acce"]["ax"]                                                              # accelerometer measurements
    acceY = sensor_output["acce"]["ay"]
    acceZ = sensor_output["acce"]["az"]

    gyroX = sensor_output["gyro"]["gx"]                                                              # gyroscope measurements in rad/s
    gyroY = sensor_output["gyro"]["gy"]
    gyroZ = sensor_output["gyro"]["gz"]

    magnX = sensor_output["magn"]["mx"]                                                              # magnetometer measurements
    magnY = sensor_output["magn"]["my"]
    magnZ = sensor_output["magn"]["mz"]

    # ---------------------------------------------------------------------------------------------- #

    # -------------------- axulirary variables to avoid reapeated calcualtions --------------------- #

    halfQuatW = 0.5 * QuatDirc["QuatW"]
    halfQuatX = 0.5 * QuatDirc["QuatX"]
    halfQuatY = 0.5 * QuatDirc["QuatY"]
    halfQuatZ = 0.5 * QuatDirc["QuatZ"]

    twoQuatW = 2.0 * QuatDirc["QuatW"]
    twoQuatX = 2.0 * QuatDirc["QuatX"]
    twoQuatY = 2.0 * QuatDirc["QuatY"]
    twoQuatZ = 2.0 * QuatDirc["QuatZ"]

    twob_x = 2.0 * b_x
    twob_z = 2.0 * b_z

    twob_xQuatW = 2.0 * b_x * QuatDirc["QuatW"]
    twob_xQuatX = 2.0 * b_x * QuatDirc["QuatX"]
    twob_xQuatY = 2.0 * b_x * QuatDirc["QuatY"]
    twob_xQuatZ = 2.0 * b_x * QuatDirc["QuatZ"]

    twob_zQuatW = 2.0 * b_z * QuatDirc["QuatW"]
    twob_zQuatX = 2.0 * b_z * QuatDirc["QuatX"]
    twob_zQuatY = 2.0 * b_z * QuatDirc["QuatY"]
    twob_zQuatZ = 2.0 * b_z * QuatDirc["QuatZ"]

    QuatWQuatY = QuatDirc["QuatW"] * QuatDirc["QuatY"]
    QuatXQuatZ = QuatDirc["QuatX"] * QuatDirc["QuatZ"]

    twoMagnX = 2.0 * magnX
    twoMagnY = 2.0 * magnY
    twoMagnZ = 2.0 * magnZ

    # ---------------------------------------------------------------------------------------------- #

    # -------------------------- normalise the accelerometer measurement --------------------------- #

    acceNorm = (acceX * acceX + acceY * acceY + acceZ * acceZ) ** 0.5
    acceX /= acceNorm
    acceY /= acceNorm
    acceZ /= acceNorm

    # ---------------------------------------------------------------------------------------------- #

    # --------------------------- normalise the magnetometer measurement --------------------------- #

    magnNorm = (magnX * magnX + magnY * magnY + magnZ * magnZ) ** 0.5
    magnX /= magnNorm
    magnY /= magnNorm
    magnZ /= magnNorm

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------ compute the objective function and Jacobian ------------------------- #

    f_1 = twoQuatX * QuatDirc["QuatZ"] - twoQuatW * QuatDirc["QuatY"] - acceX
    f_2 = twoQuatW * QuatDirc["QuatX"] + twoQuatY * QuatDirc["QuatZ"] - acceY
    f_3 = 1.0 - twoQuatX * QuatDirc["QuatX"] - twoQuatY * QuatDirc["QuatY"] - acceZ
    f_4 = twob_x * (0.5 - QuatDirc["QuatY"] * QuatDirc["QuatY"] - QuatDirc["QuatZ"] * QuatDirc["QuatZ"]) + twob_z * (QuatXQuatZ - QuatWQuatY) - magnX
    f_5 = twob_x * (QuatDirc["QuatX"] * QuatDirc["QuatY"] - QuatDirc["QuatW"] * QuatDirc["QuatZ"]) + twob_z * (QuatDirc["QuatW"] * QuatDirc["QuatX"] + QuatDirc["QuatY"] * QuatDirc["QuatZ"]) - magnY
    f_6 = twob_x * (QuatWQuatY + QuatXQuatZ) + twob_z * (0.5 - QuatDirc["QuatX"] * QuatDirc["QuatX"] - QuatDirc["QuatY"] * QuatDirc["QuatY"]) - magnZ

    J_11or24 = twoQuatY                                                                              # J_11 negated in matrix multiplication
    J_12or23 = 2.0 * QuatDirc["QuatZ"]
    J_13or22 = twoQuatW                                                                              # J_12 negated in matrix multiplication
    J_14or21 = twoQuatX

    J_32 = 2.0 * J_14or21                                                                            # negated in matrix multiplication
    J_33 = 2.0 * J_11or24                                                                            # negated in matrix multiplication
    J_41 = twob_zQuatY                                                                               # negated in matrix multiplication
    J_42 = twob_zQuatZ
    J_43 = 2.0 * twob_xQuatY + twob_zQuatW                                                           # negated in matrix multiplication
    J_44 = 2.0 * twob_xQuatZ - twob_zQuatX                                                           # negated in matrix multiplication
    J_51 = twob_xQuatZ - twob_zQuatX                                                                 # negated in matrix multiplication
    J_52 = twob_xQuatY + twob_zQuatW
    J_53 = twob_xQuatX + twob_zQuatZ
    J_54 = twob_xQuatW - twob_zQuatY                                                                 # negated in matrix multiplication
    J_61 = twob_xQuatY
    J_62 = twob_xQuatZ - 2.0 * twob_zQuatX
    J_63 = twob_xQuatW - 2.0 * twob_zQuatY
    J_64 = twob_xQuatX

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------ compute the gradient (matrix multiplication) ------------------------ #

    HatDotQuatW = J_14or21 * f_2 - J_11or24 * f_1 - J_41 * f_4 - J_51 * f_5 + J_61 * f_6
    HatDotQuatX = J_12or23 * f_1 + J_13or22 * f_2 - J_32 * f_3 + J_42 * f_4 + J_52 * f_5 + J_62 * f_6
    HatDotQuatY = J_12or23 * f_2 - J_33 * f_3 - J_13or22 * f_1 - J_43 * f_4 + J_53 * f_5 + J_63 * f_6
    HatDotQuatZ = J_14or21 * f_1 + J_11or24 * f_2 - J_44 * f_4 - J_54 * f_5 + J_64 * f_6

    # ------------ normalise the gradient to estimate direction of the gyroscope error ------------- #

    gradNorm = (HatDotQuatW * HatDotQuatW + HatDotQuatX * HatDotQuatX + HatDotQuatY * HatDotQuatY + HatDotQuatZ * HatDotQuatZ) ** 0.5
    HatDotQuatW = HatDotQuatW / gradNorm
    HatDotQuatX = HatDotQuatX / gradNorm
    HatDotQuatY = HatDotQuatY / gradNorm
    HatDotQuatZ = HatDotQuatZ / gradNorm

    # ---------------------------------------------------------------------------------------------- #

    # ----------------- compute angular estimated direction of the gyroscope error ----------------- #

    w_err_x = twoQuatW * HatDotQuatX - twoQuatX * HatDotQuatW - twoQuatY * HatDotQuatZ + twoQuatZ * HatDotQuatY
    w_err_y = twoQuatW * HatDotQuatY + twoQuatX * HatDotQuatZ - twoQuatY * HatDotQuatW - twoQuatZ * HatDotQuatX
    w_err_z = twoQuatW * HatDotQuatZ - twoQuatX * HatDotQuatY + twoQuatY * HatDotQuatX - twoQuatZ * HatDotQuatW

    # ---------------------------------------------------------------------------------------------- #

    # -------------------------- compute and remove the gyroscope baises --------------------------- #

    w_bx += w_err_x * deltat * zeta
    w_by += w_err_y * deltat * zeta
    w_bz += w_err_z * deltat * zeta

    gyroX -= w_bx
    gyroY -= w_by
    gyroZ -= w_bz

    # --------------------- compute the quaternion rate measured by gyroscopes --------------------- #

    DotOmegaQuatW = -halfQuatX * gyroX - halfQuatY * gyroY - halfQuatZ * gyroZ
    DotOmegaQuatX = halfQuatW * gyroX + halfQuatY * gyroZ - halfQuatZ * gyroY
    DotOmegaQuatY = halfQuatW * gyroY - halfQuatX * gyroZ + halfQuatZ * gyroX
    DotOmegaQuatZ = halfQuatW * gyroZ + halfQuatX * gyroY - halfQuatY * gyroX

    # ---------------------------------------------------------------------------------------------- #

    # -------------------- compute then integrate the estimated quaternion rate -------------------- #

    QuatDirc["QuatW"] += (DotOmegaQuatW - (beta * HatDotQuatW)) * deltat
    QuatDirc["QuatX"] += (DotOmegaQuatX - (beta * HatDotQuatX)) * deltat
    QuatDirc["QuatY"] += (DotOmegaQuatY - (beta * HatDotQuatY)) * deltat
    QuatDirc["QuatZ"] += (DotOmegaQuatZ - (beta * HatDotQuatZ)) * deltat

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------------------ normalise quaternion ------------------------------------ #

    QuatNorm = (QuatDirc["QuatW"] * QuatDirc["QuatW"] + QuatDirc["QuatX"] * QuatDirc["QuatX"] + QuatDirc["QuatY"] * QuatDirc["QuatY"] + QuatDirc["QuatZ"] * QuatDirc["QuatZ"]) ** 0.5
    QuatDirc["QuatW"] /= QuatNorm
    QuatDirc["QuatX"] /= QuatNorm
    QuatDirc["QuatY"] /= QuatNorm
    QuatDirc["QuatZ"] /= QuatNorm

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------------ compute flux in the earth frame ------------------------------- #

    QuatWQuatX = QuatDirc["QuatW"] * QuatDirc["QuatX"]                                               # recompute axulirary variables
    QuatWQuatY = QuatDirc["QuatW"] * QuatDirc["QuatY"]
    QuatWQuatZ = QuatDirc["QuatW"] * QuatDirc["QuatZ"]
    QuatYQuatZ = QuatDirc["QuatY"] * QuatDirc["QuatZ"]
    QuatXQuatY = QuatDirc["QuatX"] * QuatDirc["QuatY"]
    QuatXQuatZ = QuatDirc["QuatX"] * QuatDirc["QuatZ"]

    h_x = twoMagnX * (0.5 - QuatDirc["QuatY"] * QuatDirc["QuatY"] - QuatDirc["QuatZ"] * QuatDirc["QuatZ"]) + twoMagnY * (QuatXQuatY - QuatWQuatZ) + twoMagnZ * (QuatXQuatZ + QuatWQuatY)
    h_y = twoMagnX * (QuatXQuatY + QuatWQuatZ) + twoMagnY * (0.5 - QuatDirc["QuatX"] * QuatDirc["QuatX"] - QuatDirc["QuatZ"] * QuatDirc["QuatZ"]) + twoMagnZ * (QuatYQuatZ - QuatWQuatX)
    h_z = twoMagnX * (QuatXQuatZ - QuatWQuatY) + twoMagnY * (QuatYQuatZ + QuatWQuatX) + twoMagnZ * (0.5 - QuatDirc["QuatX"] * QuatDirc["QuatX"] - QuatDirc["QuatY"] * QuatDirc["QuatY"])

    # ---------------------------------------------------------------------------------------------- #

    # -------------- normalise the flux vector to have only components in the x and z -------------- #

    b_x = ((h_x * h_x) + (h_y * h_y)) ** 0.5
    b_z = h_z

    # ---------------------------------------------------------------------------------------------- #

    return QuatDirc, h_x, h_y, h_z


if __name__ == '__main__':
    from time import sleep
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read
    from Delta_Time import calculate_delta_time

    sensor = sensor_initialize("lsm9ds1")

    delta_time, Hz, current_delta_time = calculate_delta_time()

    while True:

        delta_time, Hz, current_delta_time = calculate_delta_time(current_delta_time, Hz)

        p, h_x, h_y, h_z = RCSQB_AGM(sensor_read(sensor), delta_time)
        print(p, h_x, h_y, h_z, Hz)
        print("QuatW: %-15s" % round(p["QuatW"], 3),
              "QuatX: %-15s" % round(p["QuatX"], 3),
              "QuatY: %-15s" % round(p["QuatY"], 3),
              "QuatZ: %-15s" % round(p["QuatZ"], 3),
              "h_x: %-15s" % round(h_x, 3),
              "h_y: %-15s" % round(h_y, 3),
              "h_z: %-15s" % round(h_z, 3),
              "Hz: %-15s" % round(Hz, 3),
              )
