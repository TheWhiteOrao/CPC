from Factorial import factorial


# Sinus, is be used to calculate the sinus in degrees
# returns sinus in degrees very fast but not quite so accurate, but still enough

def sinus(sinus_x, pi=3.141592653589):

    sinus_radial = (sinus_x * pi) / 180

    sinus_result = 0

    for intervals in range(0, 19):  # range must end on a non-even number and start at 0

        sinus_funktion = (sinus_radial ** (2 * intervals + 1)) / factorial(2 * intervals + 1)
        sign_switcher = (-1)**(intervals)
        sinus_result += sinus_funktion * sign_switcher

    return round(sinus_result, 10)


if __name__ == '__main__':

    print(sinus(300))
