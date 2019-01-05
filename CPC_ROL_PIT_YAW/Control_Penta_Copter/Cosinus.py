from Factorial import factorial


# Cosinus, is be used to calculate the cosinus in degrees
# returns cosinus in degrees very fast but not quite so accurate, but still enough

def cosinus(cosinus_x, pi=3.141592653589):

    cosinus_radial = (cosinus_x * pi) / 180

    cosinus_result = 1

    for intervals in range(1, 20):  # range must end on a even number and start at 1

        cosinus_funktion = (cosinus_radial ** (2 * intervals)) / factorial(2 * intervals)
        sign_switcher = (-1)**(intervals)
        cosinus_result += cosinus_funktion * sign_switcher

    return round(cosinus_result, 10)


if __name__ == '__main__':

    print(cosinus(300))
