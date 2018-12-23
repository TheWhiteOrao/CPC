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
from CPC_NAVIO2.leds import *
from CPC_NAVIO2.pwm import *

main_loop = True
led_time = 0
engine_min = 1.100
engine_max = 1.940
engine_cp = 0.25
engine_range = engine_max - engine_min
engine_cs = engine_range * (1 - engine_cp) + engine_min
engine_cp_range = engine_range * engine_cp


# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
#  ██████  ██████  ██████  ██████  ████████ ███████ ██████      ██ ███    ██ ██ ████████ ██  █████  ██      ██ ███████ ███████
# ██      ██    ██ ██   ██ ██   ██    ██    ██      ██   ██     ██ ████   ██ ██    ██    ██ ██   ██ ██      ██    ███  ██
# ██      ██    ██ ██████  ██████     ██    █████   ██████      ██ ██ ██  ██ ██    ██    ██ ███████ ██      ██   ███   █████
# ██      ██    ██ ██      ██         ██    ██      ██   ██     ██ ██  ██ ██ ██    ██    ██ ██   ██ ██      ██  ███    ██
#  ██████  ██████  ██      ██         ██    ███████ ██   ██     ██ ██   ████ ██    ██    ██ ██   ██ ███████ ██ ███████ ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

engine_one_x = 90
engine_one_y = 0

engine_two_x = 18
engine_two_y = 72

engine_thr_x = 54
engine_thr_y = 36

engine_fou_x = 54
engine_fou_y = 36

engine_fiv_x = 18
engine_fiv_y = 72


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

    if led_time == 1000:
        Led().setColor('Green')
    if led_time == 2000:
        Led().setColor('Black')
        led_time = 0

    led_time += 1

    left_y_signal = RC(RR(0), engine_min, engine_cs)
    left_x_signal = RC(RR(3), -engine_cp_range, engine_cp_range)
    right_x_signal = RC(RR(1), -engine_cp_range, engine_cp_range)
    right_y_signal = RC(RR(2), -engine_cp_range, engine_cp_range)

    engine_one_pwm.set_duty_cycle(left_y_signal)
    engine_two_pwm.set_duty_cycle(left_y_signal)
    engine_thr_pwm.set_duty_cycle(left_y_signal)
    engine_fou_pwm.set_duty_cycle(left_y_signal)
    engine_fiv_pwm.set_duty_cycle(left_y_signal)
    engine_six_pwm.set_duty_cycle(left_y_signal)

    print("left_x: %f  " % left_x_signal,
          "left_y: %f  " % left_y_signal,
          "right_x: %f  " % right_x_signal,
          "right_y: %f  " % right_y_signal)
