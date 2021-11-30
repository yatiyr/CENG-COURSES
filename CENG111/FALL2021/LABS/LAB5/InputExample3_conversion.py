"""
    This script reads a Celsius temperature
    value from the user and prints the temperature
    in Fahrenheit
"""

C = float(input("Temperature in Celsius: "))
F = C * 9.0/5.0 + 32
print(C,'Celsius is', F, 'Fahrenheit')