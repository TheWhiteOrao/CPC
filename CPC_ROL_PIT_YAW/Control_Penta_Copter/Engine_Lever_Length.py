from Sinus import sinus
from Cosinus import cosinus


#

def engine_lever_length(number_of_engien, radius_of_engien=500, engine_type="x"):
    if number_of_engien <= 1:
        pass
    else:

        distance_angel = 360 / number_of_engien

        if engine_type == "x":
            temp = distance_angel / 2
        elif engine_type == "+":
            temp = 0

        x = list(map(lambda x: 0, range(number_of_engien)))
        y = list(map(lambda x: 0, range(number_of_engien)))

        for i in range(number_of_engien):

            # print("x:", round(sinus(temp) * radius_of_engien, 12), "y:", round(cosinus(temp) * 500, 12))
            x[i] = round(sinus(temp) * radius_of_engien, 12)
            y[i] = round(cosinus(temp) * radius_of_engien, 12)

            temp += distance_angel

        return x, y


if __name__ == '__main__':
    print(engine_lever_length(5, 500, "x"))
