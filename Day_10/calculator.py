""" Calculator """


# Calculator

def add(n1, n2):
    """
    Adds two numbers together and returns the result.

    Parameters:
    a (int or float): The first number to be added.
    b (int or float): The second number to be added.

    Returns:
    The sum of a and b.
    """
    return n1 + n2


def substract(n1, n2):
    """
    Subtracts one number from another and returns the result.

    Parameters:
    a (int or float): The number to be subtracted from.
    b (int or float): The number to subtract.

    Returns:
    The difference of a minus b.
    """
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two numbers together and returns the result.

    Parameters:
    a (int or float): The first number to be multiplied.
    b (int or float): The second number to be multiplied.

    Returns:
    The product of a and b."""
    return n1 * n2


def divide(n1, n2):
    """Divides one number by another and returns the result.

    Parameters:
    a (int or float): The number to be divided.
    b (int or float): The number to divide by.

    Returns:
    The quotient of a divided by b.
    """
    return n1 / n2


operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation from the line above:")
num2 = int(input("What's the second number?: "))

calculation_function = operation[operation_symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")