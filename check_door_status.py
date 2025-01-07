# Program to check access code
access_code = "1234"
entered_code = input("Enter the access code: ")

if entered_code == access_code:
    print("The door is open.")
else:
    print("Access denied!")
