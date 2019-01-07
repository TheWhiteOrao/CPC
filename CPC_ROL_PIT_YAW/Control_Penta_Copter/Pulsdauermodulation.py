from N2.pwm import *


def pulsdauermodulation(number_of_engien, refresh_frequency=500, pos_range_max=1100, pos_range_may=1940):

    engine = dict(map(lambda x: (x, 0), range(number_of_engien)))

    for i in range(number_of_engien):
        engine[i] = PWM(i)
        engine[i].initialize()
        engine[i].set_period(refresh_frequency)
        engine[i].enable()

    print(engine)


if __name__ == '__main__':
    pulsdauermodulation(5)
