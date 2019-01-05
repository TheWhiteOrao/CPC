from N2.leds import Led()


# LED Control, can be used to turn on the led in one color and visualize that the program is running
# Static LED, can be used to turn on the led in one color
# Looping LED, can be used to visualize that the program is running, through the flashing LED in different colors

led = Led()
loop_counter = 0


def static_LED(set_first_color):

    led.setColor(set_first_color)


def looping_LED(set_first_color, set_second_color, set_interval=200):

    global loop_counter

    if loop_counter > set_interval * 2:
        loop_counter = 0

    if loop_counter < set_interval:
        led.setColor(set_first_color)

    if loop_counter >= set_interval and loop_counter < set_interval * 2:
        led.setColor(set_second_color)

    loop_counter += 1


if __name__ == '__main__':

    for i in range(1400):
        looping_LED("Black", "Cyan", 100)

    static_LED("Magenta")
