"""
    This script takes a lowercase
    letter from english alphabet
    and turns it into uppercase 
"""

lowercaseLetter = input("Lowercase Letter: ")

uppercaseLetter = chr(ord(lowercaseLetter) - 32)

print("Capitalized letter is ", uppercaseLetter)