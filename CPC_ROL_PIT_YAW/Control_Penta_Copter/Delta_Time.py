from time import perf_counter_ns


def calculate_delta_time(previous_delta_time=0, Hz=0):

    current_delta_time = perf_counter_ns()

    Hz = 1000000000 / (current_delta_time - previous_delta_time)

    delta_time = (current_delta_time - previous_delta_time) / 1000000000

    return delta_time, Hz, current_delta_time


if __name__ == '__main__':
    delta_time, Hz, current_delta_time = calculate_delta_time()

    for i in range(10000000):
        delta_time, Hz, current_delta_time = calculate_delta_time(current_delta_time, Hz)
        print(delta_time, Hz, current_delta_time)
