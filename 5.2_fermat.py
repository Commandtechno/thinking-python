def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print("holy smokes, fermat was wrong")
    else:
        print("no, that doesn't work")


check_fermat(3987, 4365, 4472, 12)
