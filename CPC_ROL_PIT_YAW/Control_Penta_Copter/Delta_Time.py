from time import process_time_ns


def delta_time(previous_delta_time=0)
    Hz = (1000000000 / (process_time_ns() - previous_delta_time))

    delta_time = (process_time_ns() - previous_delta_time) / 1000000000

    return delta_time, Hz
