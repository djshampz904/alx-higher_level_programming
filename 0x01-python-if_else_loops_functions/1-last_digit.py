#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = abs(number) % 10
if (lastnumber > 5):
    print(f"Last digit of {number} is {lastnumber} and is greater than 5")
elif (lastnumber < 6 and lastnumber != 0):
    print(f"Last digit of {number} is {lastnumber} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastnumber} and is 0")
