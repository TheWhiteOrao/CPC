from Engine_Force_Calculate import engine_force_calculate


def stabilization_controller(current_converted_receiver, previous_converted_receiver):
    engine_output = []

    angle_white = current_converted_receiver - previous_converted_receiver

    print(angle_white)

    return engine_output, current_converted_receiver


if __name__ == '__main__':

    stabilization_controller(2, 30)
