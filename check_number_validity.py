# Program to check if a number is positive, negative, or invalid
try:
    number = float(input("Enter a number: "))
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input!")
