#!/usr/bin/python3
import sys

# Function Description: Computes the factorial of an integer.
def factorial(n):
    # Parameters:
    # - n: Integer for which factorial is to be computed.

    # Returns:
    # - The factorial of n.
    
    # Base condition: if n is 0, return 1 as the factorial of 0 is 1.
    if n == 0:
        return 1
    else:
        # Recursion: return n multiplied by the factorial of (n-1).
        return n * factorial(n-1)

# Compute the factorial of the integer passed as argument in the command line.
f = factorial(int(sys.argv[1]))
print(f)
