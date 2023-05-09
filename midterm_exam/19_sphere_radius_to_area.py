import math


def sphere_surface_area(r):
    return math.pi * r * r * 4


r = int(input("Enter radius: "))
print("Surface Area:", sphere_surface_area(r))
