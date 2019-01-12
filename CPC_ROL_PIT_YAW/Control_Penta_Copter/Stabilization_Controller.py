from Engine_Force_Calculate import engine_force_calculate


def stabilization_controller(current_converted_receiver, IMU):
    pass


if __name__ == '__main__':
        from Receiver_Input import receiver_imput
        from Receiver_Signal_Converter import receiver_signal_converter
    from time import process_time_ns

    ns = 0
    IMU = {roll: 0, pitch: 0}

    while True:

        outputs = receiver_signal_converter(receiver_imput({0: (0, 1), 1: (-1, 1), 2: (-1, 1), 3: (-1, 1)}))
        zero = stabilization_controller(outputs, IMU)

        print((process_time_ns() - ns) * 0.000000001)
        ns = process_time_ns()
