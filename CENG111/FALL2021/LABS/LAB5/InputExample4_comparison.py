"""
    This script compares two values taken
    from the user and prints True if they
    are equal and prints False otherwise.
"""

# We are going to use an epsilon value for comparison
epsilon = 0.000001
a = eval(input("expression 1: "))
b = eval(input("expression 2: "))

difference = abs(a-b)
print(difference < epsilon)