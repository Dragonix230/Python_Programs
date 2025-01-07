# Program to convert binary to decimal
binary = input("Enter a binary number: ")

try:
    decimal = int(binary, 2)
    print(f"Decimal equivalent: {decimal}")
except ValueError:
    print("Invalid binary number!")
