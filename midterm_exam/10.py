def while_loop(low, high):
    x = low
    while x <= high:
        print("x:", x, "x squared:", x ** 2, "x cubed:", x ** 3)
        x += 1


def for_loop(low, high):
    for x in range(low, high + 1):
        print("x:", x, "x squared:", x ** 2, "x cubed:", x ** 3)


while_loop(int(input("Enter low: ")), int(input("Enter high: ")))
for_loop(int(input("Enter low: ")), int(input("Enter high: ")))
