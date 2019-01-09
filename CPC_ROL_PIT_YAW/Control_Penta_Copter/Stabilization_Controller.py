from Engine_Force_Calculate import engine_force_calculate


def stabilization_controller(current_converted_receiver, previous_converted_receiver, first):

    angle_white = {}

    if first == 1:
        for i in current_converted_receiver:

            angle_white[i] = current_converted_receiver[i] - previous_converted_receiver[i]

        print(angle_white)

    return angle_white, current_converted_receiver


if __name__ == '__main__':
    from Receiver_Input import receiver_imput
    from Receiver_Signal_Converter import receiver_signal_converter
    from time import process_time_ns

    previous_converted_receiver = {}
    first = 0
    ns = 0
    while True:

        outputs = receiver_signal_converter(receiver_imput({0: (0, 1), 1: (-1, 1), 2: (-1, 1), 3: (-1, 1)}))
        angle_white, previous_converted_receiver = stabilization_controller(outputs, previous_converted_receiver, first)
        print(1000000000 / (process_time_ns() - h))
        ns = process_time_ns()

        if first == 0:
            first = 1
