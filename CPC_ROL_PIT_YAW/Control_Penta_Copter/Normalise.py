
def normalise(normaDict):

    NormOut = 0

    for norm in normaDict:
        NormOut += normaDict[norm] * normaDict[norm]

    NormOut **= 0.5

    for norm in normaDict:
        normaDict[norm] /= NormOut

    return normaDict


if __name__ == '__main__':

    acceW = 0.1
    acceX = 0
    acceY = 0.3
    acceZ = 0.9

    q = normalise({"acceW": acceW, "acceX": acceX, "acceY": acceY, "acceZ": acceZ})

    print(q["acceW"], q["acceX"], q["acceY"], q["acceZ"])
