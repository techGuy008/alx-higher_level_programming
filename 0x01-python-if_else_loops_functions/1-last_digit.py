#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    postStr = "and is greater than 5"
elif last == 0:
    postStr = "and is 0"
else:
    postStr = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last} {postStr}")