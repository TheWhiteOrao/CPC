from CPC_NAVIO2.lsm9ds1 import *
from CPC_NAVIO2.mpu9250 import *
from CPC_NAVIO2.ms5611 import *


lsm9ds1 = LSM9DS1()
mpu9250 = MPU9250()
ms5611 = MS5611()

lsm9ds1.initialize()
mpu9250.initialize()
ms5611.initialize()

while True:
    ms5611.refreshPressure()

    ms5611.readPressure()

    ms5611.refreshTemperature()

    ms5611.readTemperature()

    ms5611.calculatePressureAndTemperature()

    print("Temperature(C): %.6f" % (ms5611.TEMP), "Pressure(millibar): %.6f" % (ms5611.PRES))
