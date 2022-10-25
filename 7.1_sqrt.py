import math


def mysqrt(a):
    x = 10
    while True:
        if x == 0:
            return x
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def test_square_root():
    print("a", "|", "mysqrt(a)", "|", "math.sqrt(a)", "|", "diff")
    for a in range(10):
        print(a, "|", mysqrt(a), "|", math.sqrt(a), "|", mysqrt(a) - math.sqrt(a))


test_square_root()
