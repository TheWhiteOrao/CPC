from N2.pwm import *


def pulsdauermodulation(number_of_engien):

    engine = dict(map(lambda x: (x, 0), range(number_of_engien)))

    for i in range(number_of_engien):
        engine[i] = PWM(i)

    print(engine)

    for i in range(number_of_engien):
        engine[i].initialize()

    print(engine)


if __name__ == '__main__':
    pulsdauermodulation(5)
