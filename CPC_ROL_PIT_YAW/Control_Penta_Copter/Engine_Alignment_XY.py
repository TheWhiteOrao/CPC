
def engine_alignment_xy(x, y, angel):

    engine_alignment = {"y+": {}, "x+": {}, "y-": {}, "x-": {}}

    for i in range(len(angel)):

        if angel[i] < 90 or angel[i] > 270:
            engine_alignment["y+"][i] = y[i]

        if angel[i] > 0 and angel[i] < 180:
            engine_alignment["x+"][i] = x[i]

        if angel[i] > 90 and angel[i] < 270:
            engine_alignment["y-"][i] = y[i]

        if angel[i] > 180:
            engine_alignment["x-"][i] = x[i]

    return engine_alignment


if __name__ == '__main__':
    x = {0: 0.0, 1: 475.52825815, 2: 293.89262615, 3: -293.89262615, 4: -475.52825815}
    y = {0: 500.0, 1: 154.5084972, 2: -404.5084972, 3: -404.5084972, 4: 154.5084972}
    angels = {0: 0, 1: 72.0, 2: 144.0, 3: 216.0, 4: 288.0}

    print(engine_alignment_xy(x, y, angels))
