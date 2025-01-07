# Program to print "Yatzy" if dice number is 6
import random

while True:
    dice_number = random.randint(1, 6)
    print(f"Dice rolled: {dice_number}")
    if dice_number == 6:
        print("Yatzy!")
        break
