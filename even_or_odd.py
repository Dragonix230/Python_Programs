# Program to check if a number is even or odd
try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("Invalid input! Please enter an integer.")