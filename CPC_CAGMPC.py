from CPC_NAVIO2.lsm9ds1 import *
from CPC_NAVIO2.mpu9250 import *
from CPC_NAVIO2.ms5611 import *
from time import *

lsm9ds1 = LSM9DS1()
mpu9250 = MPU9250()
ms5611 = MS5611()

null_p = 0

lsm9ds1.initialize()
mpu9250.initialize()
ms5611.initialize()

for i in range(1, 110):
    if i >= 10:
        ms5611.refreshPressure()
        sleep(0.01)
        ms5611.readPressure()

        ms5611.refreshTemperature()
        sleep(0.01)
        ms5611.readTemperature()

        ms5611.calculatePressureAndTemperature()

        null_p += ms5611.PRES / 100

while True:
    Tempr = 0

    for i in range(20):
        ms5611.refreshPressure()
        sleep(0.01)  # Waiting for pressure data ready
        ms5611.readPressure()

        ms5611.refreshTemperature()
        sleep(0.01)  # Waiting for temperature data ready
        ms5611.readTemperature()

        ms5611.calculatePressureAndTemperature()

        Tempr += ((null_p - ms5611.PRES) * 9.3) / 20

    print("Temperature(C): %.6f" % (ms5611.TEMP), "Pressure(millibar): %.6f" % (Tempr))
