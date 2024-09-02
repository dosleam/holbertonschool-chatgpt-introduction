#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer n using recursion.

    Function Description:
    This function computes the factorial of the given integer `n` using a recursive approach.
    The factorial of a non-negative integer n is defined as the product of all positive integers
    less than or equal to n. By definition, the factorial of 0 is 1.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer `n`. If n is 0, the function returns 1.

    Example:
    factorial(4)  # Returns 24 because 4! = 4 * 3 * 2 * 1 = 24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Parse the integer from the command-line argument, calculate the factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
