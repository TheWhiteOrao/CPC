from time import process_time_ns


def calculate_delta_time(previous_delta_time=1):
    current_delta_time = process_time_ns()

    delta_time = (current_delta_time - previous_delta_time) / 1000000000

    return delta_time, current_delta_time


if __name__ == '__main__':

    delta_time, current_delta_time = calculate_delta_time()

    for i in range(10000):
        delta_time,  current_delta_time = calculate_delta_time(current_delta_time)
        # print(delta_time, current_delta_time)
        try:
            print(1 / delta_time)
        except:
            pass

        for i in range(1000):
            h = i ** i
