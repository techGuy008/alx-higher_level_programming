#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        txt = i
        if i % 3 == 0 and i % 5 == 0:
           txt = "FizzBuzz "
        elif i % 3 == 0:
            txt = "Fizz "
        elif i % 5 == 0:
            txt = "Buzz "
        print("{} ".format(txt), end="")
