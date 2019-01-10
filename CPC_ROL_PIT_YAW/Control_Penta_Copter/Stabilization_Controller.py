from Engine_Force_Calculate import engine_force_calculate


def stabilization_controller(current_converted_receiver, angle_white, first):

    if first == 1:
        for i in current_converted_receiver:

            angle_white[i] += 75 * current_converted_receiver[i]

    if first == 0:

        for i in current_converted_receiver:
            angle_white[i] = 0

    return angle_white, current_converted_receiver


if __name__ == '__main__':
    from Receiver_Input import receiver_imput
    from Receiver_Signal_Converter import receiver_signal_converter
    from time import process_time_ns

    first = 0
    ns = 0
    angle_white = {}
    while True:

        outputs = receiver_signal_converter(receiver_imput({0: (0, 1), 1: (-1, 1), 2: (-1, 1), 3: (-1, 1)}))
        angle_white, previous_converted_receiver = stabilization_controller(outputs, angle_white, first)
        print(angle_white, 1000000000 / (process_time_ns() - ns))
        ns = process_time_ns()

        if first == 0:
            first = 1
