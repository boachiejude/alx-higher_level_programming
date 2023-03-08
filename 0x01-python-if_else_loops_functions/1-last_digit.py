#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print("Last digit of {} is".format(number), end=" ")
print("{} and is".format(number % 10), end=" ")

if number > 5:
    print("greater than 5")
elif number == 0:
    print("0")
else:
    print("less than 6 and not 0")
print("\n")
