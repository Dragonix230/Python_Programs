# Program to check if a number is prime using while loop
number = int(input("Enter a number: "))

if number < 2:
    print("Not a prime number.")
else:
    is_prime = True
    i = 2
    while i * i <= number:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("The number is prime.")
    else:
        print("Not a prime number.")
