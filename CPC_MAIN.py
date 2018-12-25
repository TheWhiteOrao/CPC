# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███    ███  █████  ██ ███    ██     ██████  ██████   ██████   ██████  ██████   █████  ███    ███ ███    ███
# ████  ████ ██   ██ ██ ████   ██     ██   ██ ██   ██ ██    ██ ██       ██   ██ ██   ██ ████  ████ ████  ████
# ██ ████ ██ ███████ ██ ██ ██  ██     ██████  ██████  ██    ██ ██   ███ ██████  ███████ ██ ████ ██ ██ ████ ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██  ██  ██ ██  ██  ██
# ██      ██ ██   ██ ██ ██   ████     ██      ██   ██  ██████   ██████  ██   ██ ██   ██ ██      ██ ██      ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

from CPC_RR import *
from CPC_RC import *
from CPC_CO import *
from CPC_NAVIO2.leds import *
from CPC_NAVIO2.pwm import *
from CPC_NAVIO2.adc import *

main_loop = True
led_time = 0
engine_min = 1.100
engine_max = 1.940
engine_cp = 0.25
engine_e = 0.45
engine_range = engine_max - engine_min
engine_cs = engine_range * (1 - engine_cp) + engine_min
adc = ADC()

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
#  ██████  ██████  ██████  ██████  ████████ ███████ ██████      ██ ███    ██ ██ ████████ ██  █████  ██      ██ ███████ ███████
# ██      ██    ██ ██   ██ ██   ██    ██    ██      ██   ██     ██ ████   ██ ██    ██    ██ ██   ██ ██      ██    ███  ██
# ██      ██    ██ ██████  ██████     ██    █████   ██████      ██ ██ ██  ██ ██    ██    ██ ███████ ██      ██   ███   █████
# ██      ██    ██ ██      ██         ██    ██      ██   ██     ██ ██  ██ ██ ██    ██    ██ ██   ██ ██      ██  ███    ██
#  ██████  ██████  ██      ██         ██    ███████ ██   ██     ██ ██   ████ ██    ██    ██ ██   ██ ███████ ██ ███████ ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
rotor_radius = 500
engine_force = 10000

basic_lever = engine_force * rotor_radius

# engine_one_x = 90
engine_one_y = 0

engine_two_x = 18
engine_two_y = 72

engine_thr_x = 54
engine_thr_y = 36

engine_fou_x = 54
engine_fou_y = 36

engine_fiv_x = 18
engine_fiv_y = 72

# engine_one_length_to_x = CO(engine_one_x) * rotor_radius
engine_one_length_to_y = CO(engine_one_y) * rotor_radius

engine_two_length_to_x = CO(engine_two_x) * rotor_radius
engine_two_length_to_y = CO(engine_two_y) * rotor_radius

engine_thr_length_to_x = CO(engine_thr_x) * rotor_radius
engine_thr_length_to_y = CO(engine_thr_y) * rotor_radius

engine_fou_length_to_x = CO(engine_fou_x) * rotor_radius
engine_fou_length_to_y = CO(engine_fou_y) * rotor_radius

engine_fiv_length_to_x = CO(engine_fiv_x) * rotor_radius
engine_fiv_length_to_y = CO(engine_fiv_y) * rotor_radius

# engine_one_lever_x = basic_lever / (engine_one_length_to_x * engine_force)
engine_one_lever_y = basic_lever / (engine_one_length_to_y * engine_force)

engine_two_lever_x = basic_lever / (engine_two_length_to_x * engine_force)
engine_two_lever_y = basic_lever / (engine_two_length_to_y * engine_force)

engine_thr_lever_x = basic_lever / (engine_thr_length_to_x * engine_force)
engine_thr_lever_y = basic_lever / (engine_thr_length_to_y * engine_force)

engine_fou_lever_x = basic_lever / (engine_fou_length_to_x * engine_force)
engine_fou_lever_y = basic_lever / (engine_fou_length_to_y * engine_force)

engine_fiv_lever_x = basic_lever / (engine_fiv_length_to_x * engine_force)
engine_fiv_lever_y = basic_lever / (engine_fiv_length_to_y * engine_force)


# f = engine_125

engine_one_f = engine_one_lever_y / 3
engine_two_f = engine_two_lever_y / 3
engine_fiv_f = engine_fiv_lever_y / 3

# r = engine_23

engine_two_r = engine_two_lever_x / 2
engine_thr_r = engine_thr_lever_x / 2

# b = engine_34

engine_thr_b = engine_thr_lever_y / 2
engine_fou_b = engine_fou_lever_y / 2

# l = engine 45

engine_fou_l = engine_fou_lever_x / 2
engine_fiv_l = engine_fiv_lever_x / 2


# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███████ ███    ██  ██████  ██ ███    ██ ███████     ██ ███    ██ ██ ████████ ██  █████  ██      ██ ███████ ███████
# ██      ████   ██ ██       ██ ████   ██ ██          ██ ████   ██ ██    ██    ██ ██   ██ ██      ██    ███  ██
# █████   ██ ██  ██ ██   ███ ██ ██ ██  ██ █████       ██ ██ ██  ██ ██    ██    ██ ███████ ██      ██   ███   █████
# ██      ██  ██ ██ ██    ██ ██ ██  ██ ██ ██          ██ ██  ██ ██ ██    ██    ██ ██   ██ ██      ██  ███    ██
# ███████ ██   ████  ██████  ██ ██   ████ ███████     ██ ██   ████ ██    ██    ██ ██   ██ ███████ ██ ███████ ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

engine_one_pwm = PWM(0)
engine_two_pwm = PWM(1)
engine_thr_pwm = PWM(2)
engine_fou_pwm = PWM(3)
engine_fiv_pwm = PWM(4)
engine_six_pwm = PWM(5)

engine_one_pwm.initialize()
engine_two_pwm.initialize()
engine_thr_pwm.initialize()
engine_fou_pwm.initialize()
engine_fiv_pwm.initialize()
engine_six_pwm.initialize()

engine_one_pwm.set_period(500)
engine_two_pwm.set_period(500)
engine_thr_pwm.set_period(500)
engine_fou_pwm.set_period(500)
engine_fiv_pwm.set_period(500)
engine_six_pwm.set_period(500)

engine_one_pwm.enable()
engine_two_pwm.enable()
engine_thr_pwm.enable()
engine_fou_pwm.enable()
engine_fiv_pwm.enable()
engine_six_pwm.enable()

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███    ███  █████  ██ ███    ██     ██       ██████   ██████  ██████
# ████  ████ ██   ██ ██ ████   ██     ██      ██    ██ ██    ██ ██   ██
# ██ ████ ██ ███████ ██ ██ ██  ██     ██      ██    ██ ██    ██ ██████
# ██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██    ██ ██    ██ ██
# ██      ██ ██   ██ ██ ██   ████     ███████  ██████   ██████  ██
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

while main_loop:

    #
    # LED
    #

    if led_time == 100:
        Led().setColor('Green')
    if led_time == 200:
        Led().setColor('Black')
        led_time = 0

    led_time += 1

    #
    # ACD
    #

    print("A0: %f V " % (adc.read(0) / 1000),
          "A2: %f V " % (adc.read(2) / 100),
          "A3: %f A " % (adc.read(3) / 100),
          )

    #
    #
    #

    left_y_signal = RC(RR(0), engine_min, engine_cs)
    left_x_signal = RC(RR(3), -engine_cp, engine_cp)

    right_x_signal = RC(RR(1), -engine_cp, engine_cp)
    right_y_signal = RC(RR(2), -engine_cp, engine_cp)

    engine_one_memory = left_y_signal
    engine_two_memory = left_y_signal
    engine_thr_memory = left_y_signal
    engine_fou_memory = left_y_signal
    engine_fiv_memory = left_y_signal
    engine_six_memory = left_y_signal

    if left_x_signal < 0:
        engine_six_memory += engine_range * (abs(left_x_signal) * engine_e)  # optional **** engine_e
    elif left_x_signal > 0:
        engine_six_memory -= engine_range * (abs(left_x_signal) * engine_e)  # optional **** engine_e

    if right_x_signal < 0:  # - to_the_left engine_r inC engine_l deC
        engine_two_memory += engine_range * (abs(right_x_signal) * (engine_two_r * engine_e))
        engine_thr_memory += engine_range * (abs(right_x_signal) * (engine_thr_r * engine_e))
        engine_fou_memory -= engine_range * (abs(right_x_signal) * (engine_fou_l * engine_e))
        engine_fiv_memory -= engine_range * (abs(right_x_signal) * (engine_fiv_l * engine_e))
    elif right_x_signal > 0:  # + to_the_right engine_r deC engine_l inC
        engine_two_memory -= engine_range * (abs(right_x_signal) * (engine_two_r * engine_e))
        engine_thr_memory -= engine_range * (abs(right_x_signal) * (engine_thr_r * engine_e))
        engine_fou_memory += engine_range * (abs(right_x_signal) * (engine_fou_l * engine_e))
        engine_fiv_memory += engine_range * (abs(right_x_signal) * (engine_fiv_l * engine_e))
    else:
        pass

    if right_y_signal < 0:  # - to_the_back engine_b deC engine_f inC
        engine_one_memory += engine_range * (abs(right_y_signal) * (engine_one_f * engine_e))
        engine_two_memory += engine_range * (abs(right_y_signal) * (engine_two_f * engine_e))
        engine_fiv_memory += engine_range * (abs(right_y_signal) * (engine_fiv_f * engine_e))

        engine_thr_memory -= engine_range * (abs(right_y_signal) * (engine_thr_b * engine_e))
        engine_fou_memory -= engine_range * (abs(right_y_signal) * (engine_fou_b * engine_e))

    elif right_y_signal > 0:  # + to_the_front engine_b inC engine_f deC
        engine_one_memory -= engine_range * (abs(right_y_signal) * (engine_one_f * engine_e))
        engine_two_memory -= engine_range * (abs(right_y_signal) * (engine_two_f * engine_e))
        engine_fiv_memory -= engine_range * (abs(right_y_signal) * (engine_fiv_f * engine_e))

        engine_thr_memory += engine_range * (abs(right_y_signal) * (engine_thr_b * engine_e))
        engine_fou_memory += engine_range * (abs(right_y_signal) * (engine_fou_b * engine_e))
    else:
        pass

    engine_one_pwm.set_duty_cycle(engine_one_memory)
    engine_two_pwm.set_duty_cycle(engine_two_memory)
    engine_thr_pwm.set_duty_cycle(engine_thr_memory)
    engine_fou_pwm.set_duty_cycle(engine_fou_memory)
    engine_fiv_pwm.set_duty_cycle(engine_fiv_memory)
    engine_six_pwm.set_duty_cycle(engine_six_memory)

    # print("left_x: %f  " % left_x_signal,
    #       "left_y: %f  " % left_y_signal,
    #       "right_x: %f  " % right_x_signal,
    #       "right_y: %f  " % right_y_signal)
