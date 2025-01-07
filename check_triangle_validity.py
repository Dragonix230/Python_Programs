# Program to check if a triangle is valid
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
