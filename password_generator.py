import random
import string

print("Python Password Generator 🔐")

# Ask for password length
length = int(input("Enter password length: "))

# Ask which type of characters to include
print("Choose character types to include:")
print("1 - Letters only")
print("2 - Letters + Numbers")
print("3 - Letters + Numbers + Symbols")

choice = input("Enter 1, 2, or 3: ")
