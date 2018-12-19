
# ███████  █████   ██████ ████████  ██████  ██████  ██  █████  ██
# ██      ██   ██ ██         ██    ██    ██ ██   ██ ██ ██   ██ ██
# █████   ███████ ██         ██    ██    ██ ██████  ██ ███████ ██
# ██      ██   ██ ██         ██    ██    ██ ██   ██ ██ ██   ██ ██
# ██      ██   ██  ██████    ██     ██████  ██   ██ ██ ██   ██ ███████


def FR(factorial):
    output_factorial = 1

    for i in range(1, factorial + 1):
        output_factorial *= i
    return output_factorial


if __name__ == '__main__':
    print(FR(5))
