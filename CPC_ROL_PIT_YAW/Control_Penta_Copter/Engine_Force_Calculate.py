from Engine_Lever_Length import engine_lever_length
from Engine_Alignment_XY import engine_alignment_xy


def engine_force_calculate(number_of_engien,  radius_of_engien, engine_type, force=1000):

    lever_force = force * radius_of_engien

    x, y, angel = engine_lever_length(number_of_engien, radius_of_engien, engine_type)

    for i in range(len(x)):

        if x[i] == 0:
            x[i] = 0
        else:
            x[i] = lever_force / (x[i] * force)

        if y[i] == 0:
            y[i] = 0
        else:
            y[i] = lever_force / (y[i] * force)

    engine_dict = engine_alignment_xy(x, y, angel)

    for direction in engine_dict:
        for engine in engine_dict[direction]:
            engine_dict[direction][engine] = abs(engine_dict[direction][engine] / (len(engine_dict[direction])))

    return engine_dict


if __name__ == '__main__':
    print(engine_force_calculate(5, 500, "+"))
