from CPC_NA2.leds import *

led = Led()
loop_counter = 0


def led_singel(color_one):
    led.setColor(color_one)


def led_loop(color_one, color_two, setinterval=200):
    global loop_counter
    if loop_counter > setinterval * 2:
        loop_counter = 0

    if loop_counter < setinterval:
        led.setColor(color_one)

    if loop_counter >= setinterval and loop_counter < setinterval * 2:
        led.setColor(color_one)

    loop_counter += 1
