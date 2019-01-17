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

deltat = 0.001                                                                                       # sampling period in seconds (shown as 1 ms)
gyroMeasError = 3.14159265358979 * (5.0 / 180.0)                                                     # gyroscope measurement error in rad/s (shown as 5 deg/s)
beta = ((3.0 / 4.0) ** 0.5) * gyroMeasError                                                          # compute beta

# -------------------------------------------------------------------------------------------------- #

# ------------------------------------ Global system variables ------------------------------------- #

QuatDirc = {"QuatW": 1.0, "QuatX": 0.0, "QuatY": 0.0, "QuatZ": 0.0}                                  # estimated orientation quaternion elements with initial conditions

# -------------------------------------------------------------------------------------------------- #


def RCSQB_AG(sensor_output):

    # ------------------------------- Global variables in RCSQB_AG --------------------------------- #

    global deltat
    global gyroMeasError
    global beta
    global QuatDirc

    # ---------------------------------------------------------------------------------------------- #

    # ------------------------- Binds sensor outputs to multiple variables ------------------------- #

    acceX = sensor_output["acce"]["ax"]
    acceY = sensor_output["acce"]["ay"]
    acceZ = sensor_output["acce"]["az"]

    gyroX = sensor_output["gyro"]["gx"]
    gyroY = sensor_output["gyro"]["gy"]
    gyroZ = sensor_output["gyro"]["gz"]

    # ---------------------------------------------------------------------------------------------- #
    # # Local system variables
    # float norm                                                                  # vector norm
    # float SEqDot_omega_1, SEqDot_omega_2, SEqDot_omega_3, SEqDot_omega_4        # quaternion derrivative from gyroscopes elements
    # float f_1, f_2, f_3                                                         # objective function elements
    # float J_11or24, J_12or23, J_13or22, J_14or21, J_32, J_33                    # objective function Jacobian elements
    # float SEqHatDot_1, SEqHatDot_2, SEqHatDot_3, SEqHatDot_4                    # estimated direction of the gyroscope error

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

    SEqDot_omega_1 = -half_QuatX * gyroX - half_QuatY * gyroY - half_QuatZ * gyroZ
    SEqDot_omega_2 = half_QuatW * gyroX + half_QuatY * gyroZ - half_QuatZ * gyroY
    SEqDot_omega_3 = half_QuatW * gyroY - half_QuatX * gyroZ + half_QuatZ * gyroX
    SEqDot_omega_4 = half_QuatW * gyroZ + half_QuatX * gyroY - half_QuatY * gyroX

    # ---------------------------------------------------------------------------------------------- #

    # Compute then integrate the estimated quaternion derrivative

    QuatDirc["QuatW"] += (SEqDot_omega_1 - (beta * QuatW_HatDot)) * deltat
    QuatDirc["QuatX"] += (SEqDot_omega_2 - (beta * QuatX_HatDot)) * deltat
    QuatDirc["QuatY"] += (SEqDot_omega_3 - (beta * QuatY_HatDot)) * deltat
    QuatDirc["QuatZ"] += (SEqDot_omega_4 - (beta * QuatZ_HatDot)) * deltat

    # ---------------------------------------------------------------------------------------------- #

    # Normalise quaternion

    quatNorm = (QuatDirc["QuatW"] * QuatDirc["QuatW"] + QuatDirc["QuatX"] * QuatDirc["QuatX"] + QuatDirc["QuatY"] * QuatDirc["QuatY"] + QuatDirc["QuatZ"] * QuatDirc["QuatZ"]) ** 0.5
    QuatDirc["QuatW"] /= quatNorm
    QuatDirc["QuatX"] /= quatNorm
    QuatDirc["QuatY"] /= quatNorm
    QuatDirc["QuatZ"] /= quatNorm

    # ---------------------------------------------------------------------------------------------- #

    return QuatDirc


if __name__ == '__main__':
    from time import sleep
    from Sensor_Initialize import sensor_initialize
    from Sensor_Read import sensor_read
    from Delta_Time import calculate_delta_time

    sensor = sensor_initialize("mpu9250")

    delta_time, Hz, current_delta_time = calculate_delta_time()

    while True:

        delta_time, Hz, current_delta_time = calculate_delta_time(current_delta_time, Hz)

        p = RCSQB_AG(sensor_read(sensor))
        print(Hz)
