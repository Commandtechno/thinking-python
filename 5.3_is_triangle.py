def is_triangle(a, b, c):
    if a > b + c or b > c + a or c > a + b:
        print("no")
    else:
        print("yes")


is_triangle(1, 1, 3)
