"""
    This script reads two integers from the user and
    prints the maximum of the two
"""

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

print(((num1+num2) + abs(num1-num2))/2)
# or print(max(num1, num2))