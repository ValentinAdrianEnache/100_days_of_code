""" Calculator """

# Calculator
from art import logo
import os



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


def calculator():
    print(logo)

    num1 = int(input("What's the first number?: "))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
