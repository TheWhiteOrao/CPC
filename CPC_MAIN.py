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


# pwm.set_period(500)
# pwm.enable()

# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████
#
# ███████ ███    ██  ██████  ██ ███    ██ ███████     ██ ███    ██ ██ ████████ ██  █████  ██      ██ ███████ ███████
# ██      ████   ██ ██       ██ ████   ██ ██          ██ ████   ██ ██    ██    ██ ██   ██ ██      ██    ███  ██
# █████   ██ ██  ██ ██   ███ ██ ██ ██  ██ █████       ██ ██ ██  ██ ██    ██    ██ ███████ ██      ██   ███   █████
# ██      ██  ██ ██ ██    ██ ██ ██  ██ ██ ██          ██ ██  ██ ██ ██    ██    ██ ██   ██ ██      ██  ███    ██
# ███████ ██   ████  ██████  ██ ██   ████ ███████     ██ ██   ████ ██    ██    ██ ██   ██ ███████ ██ ███████ ███████
#
# ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████ ███████

engine_one = PWM(0)
engine_two = PWM(1)
engine_thr = PWM(2)
engine_fou = PWM(3)
engine_fiv = PWM(4)
engine_six = PWM(5)

engine_one.initialize()
engine_two.initialize()
engine_thr.initialize()
engine_fou.initialize()
engine_fiv.initialize()
engine_six.initialize()

engine_one.set_period(500)
engine_two.set_period(500)
engine_thr.set_period(500)
engine_fou.set_period(500)
engine_fiv.set_period(500)
engine_six.set_period(500)

engine_one.enable()
engine_two.enable()
engine_thr.enable()
engine_fou.enable()
engine_fiv.enable()
engine_six.enable()

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

    left_y_signal = RC(RR(0), 1.100, 1.940)
    left_x_signal = RC(RR(3), -1, 1)
    right_x_signal = RC(RR(1), -1, 1)
    right_y_signal = RC(RR(2), -1, 1)

    engine_one.set_duty_cycle(left_y_signal)
    engine_two.set_duty_cycle(left_y_signal)
    engine_thr.set_duty_cycle(left_y_signal)
    engine_fou.set_duty_cycle(left_y_signal)
    engine_fiv.set_duty_cycle(left_y_signal)
    engine_six.set_duty_cycle(left_y_signal)

    print("left_x: %f  " % left_x_signal,
          "left_y: %f  " % left_y_signal,
          "right_x: %f  " % right_x_signal,
          "right_y: %f  " % right_y_signal)
