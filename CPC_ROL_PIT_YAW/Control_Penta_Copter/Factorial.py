

# Factorial, returns the factorial of the imput number
# For example the Factorial of 5 is 120

def factorial(number_of_factorial):

    output_factorial = 1

    for i in range(1, number_of_factorial + 1):
        output_factorial *= i

    return output_factorial


if __name__ == '__main__':

    print(factorial(5))
