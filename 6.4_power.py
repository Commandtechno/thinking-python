def is_power(a, b):
    if a == b:
        return True
    elif b == 1:
        return False

    return a % b == 0 and is_power(a / b, b)


print(is_power(8, 2))
