def is_power(a, b):
    if a == b:
        return True
    elif b == 1:
        return False

    return a % b == 0 and is_power(a / b, b)


print("This program will check if a is a power of b")
print(is_power(int(input("Enter a: ")), int(input("Enter b: "))))
