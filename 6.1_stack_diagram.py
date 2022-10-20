def b(z):
    prod = a(z, z)
    print("product of", z, "and", z + 1, "is", prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    total = x + y + z
    print("sum of", x, y, z, "is", total)
    square = b(total) ** 2
    return square


x = 1
y = x + 1
print(c(x, y + 3, x + y))
