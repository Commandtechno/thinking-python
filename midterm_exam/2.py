import math


def vol(r):
    return r**3 * math.pi * 4 / 3


n = int(input("Enter your birth month: "))
print("+5", "-", vol(n + 5))
print("+10", "-", vol(n + 10))
print("+15", "-", vol(n + 15))
print("+20", "-", vol(n + 20))
