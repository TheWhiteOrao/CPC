from CPC_NA2.leds import *

led = Led()
loop_counter = 0


def led_singel(color_one):
    led.setColor(color_one)


def led_loop(color_one, color_two, set_interval=200):
    global loop_counter
    if loop_counter > set_interval * 2:
        loop_counter = 0
        print("3")

    if loop_counter < set_interval:
        led.setColor(color_one)
        print("1", color_one)

    if loop_counter >= set_interval and loop_counter < set_interval * 2:
        led.setColor(color_two)
        print("2", color_two)

    loop_counter += 1


if __name__ == '__main__':
    for i in range(14000):
        led_loop("Black", "Green", 200)
