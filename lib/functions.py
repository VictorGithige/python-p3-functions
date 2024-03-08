#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")
    pass
greet("James")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass
greet_with_default('jerry')

def add(num1, num2):
    return num1 + num2
    pass
sum = add(23, 25)
print(sum)


def halve(number):
    return number / 2
    pass
half = halve(20)
print(half)
