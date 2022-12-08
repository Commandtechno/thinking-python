import math


def circle_area(r):
    return math.pi * r * r


def circle_circumference(r):
    return math.pi * r * 2


r = int(input("Enter radius: "))
print("Area:", circle_area(r))
print("Circumference:", circle_circumference(r))
