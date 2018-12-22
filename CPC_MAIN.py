
# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████

from CPC_RR import *
from CPC_RC import *
from CPC_NAVIO2.leds import *
from CPC_NAVIO2.pwm import *

main_loop = True
led_time = 0

pwm_out = 0
pwm_t = PWM(pwm_out)
print(pwm_t)
pwm_t.set_period(500)
pwm_t.enable()

print(pwm_t)

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

    pwm_t.set_duty_cycle(left_y_signal)

    print("left_x: %f  " % left_x_signal,
          "left_y: %f  " % left_y_signal,
          "right_x: %f  " % right_x_signal,
          "right_y: %f  " % right_y_signal)
