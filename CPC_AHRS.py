
# include <stdio.h>
# include <sys/socket.h>
# include <netinet/in.h>
# include <arpa/inet.h>
# include <stdint.h>
# include <unistd.h>


from CPC_AHRS_ import *
from CPC_NAVIO2.mpu9250 import *
from time import *

G_SI = 9.80665
PI = 3.14159


imu = MPU9250()
ahrs = AHRS()


# Timing data
offset = [0, 0, 0]
mindt = 0.01
dtsumm = 0
isFirst = 1


def usleep(x):
    return sleep(x / 1000000.0)

#= == == == == == == == == == == == == == == Initial setup == == == == == == == == == == == == == == == == =


def imuSetup():
    # ----------------------- MPU initialization - -----------------------------
    imu.initialize()
    # -------------------------------------------------------------------------
    print("Beginning Gyro calibration...\n")

    for i in range(100):

        axyz, gxyz = imu.getMotion6()
        ax = axyz[0]
        ay = axyz[1]
        az = axyz[2]

        gx = gxyz[0]
        gy = gxyz[1]
        gz = gxyz[2]

        gx *= 180 / PI
        gy *= 180 / PI
        gz *= 180 / PI

        offset[0] += (-gx * 0.0175)
        offset[1] += (-gy * 0.0175)
        offset[2] += (-gz * 0.0175)

        usleep(10000)

    offset[0] /= 100.0
    offset[1] /= 100.0
    offset[2] /= 100.0

    print("Offsets are: {0} {1} {2}\n".format(offset[0], offset[1], offset[2]))

    ahrs.setGyroOffset(offset[0], offset[1], offset[2])

#= == == == == == == == == == == == == == == = Main loop == == == == == == == == == == == == == == == == == ==


def imuLoop():

    # ----------------------- Calculate delta time - ---------------------------

    previoustime = currenttime
    currenttime = time_ns()
    dt = (currenttime - previoustime) / 1000000

    if dt < (1 / 1300):
        usleep((1 / 1300 - dt) * 1000000)

    currenttime = time_ns()
    dt = (currenttime - previoustime) / 1000000

    # -------- Read raw measurements from the MPU and update AHRS - -------------

    # Accel + gyro.
    axyz, gxyz = imu.getMotion6()
    ax = axyz[0]
    ay = axyz[1]
    az = axyz[2]

    gx = gxyz[0]
    gy = gxyz[1]
    gz = gxyz[2]

    ax /= G_SI
    ay /= G_SI
    az /= G_SI
    gx *= 180 / PI
    gy *= 180 / PI
    gz *= 180 / PI

    ahrs.updateIMU(ax, ay, az, gx * 0.0175, gy * 0.0175, gz * 0.0175, dt)

    # Accel + gyro + mag.
    # Soft and hard iron calibration required for proper function.
    #
    # imu.getMotion9(& ax, & ay, & az, & gx, & gy, & gz, & mx, & my, & mz);
    # ahrs.update(ax, ay, az, gx * 0.0175, gy * 0.0175, gz * 0.0175, my, mx, -mz, dt);
    #

    #------------------------ Read Euler angles - -----------------------------

    rpy = ahrs.getEuler()
    roll = rpy[0]
    pitch = rpy[1]
    yaw = rpy[2]

    # ------------------- Discard the time of the first cycle - ----------------

    if isFirst == 1:
        if dt > maxdt:
            maxdt = dt
        if dt < mindt:
            mindt = dt
    isFirst = 0

    # ------------- Console and network output with a lowered rate - -----------

    dtsumm += dt
    if dtsumm > 0.05:

        # Console output
        print("ROLL: %+05.2f PITCH: %+05.2f YAW: %+05.2f PERIOD %.4fs RATE %dHz \n", roll, pitch, yaw * -1, dt, int(1 / dt));

        # Network output
        # sprintf(sendline, "%10f %10f %10f %10f %dHz\n", ahrs.getW(), ahrs.getX(), ahrs.getY(), ahrs.getZ(), int(1 / dt));
        # sendto(sockfd, sendline, strlen(sendline), 0, (struct sockaddr *)&servaddr, sizeof(servaddr));

        dtsumm = 0


#= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# -------------------- IMU setup and main loop - ---------------------------

imuSetup()
while True:
    imuLoop()