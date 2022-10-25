# i gave up on this one

import math


def factorial(n):
    """Computes factorial of n recursively."""
    if n <= 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def estimate_pi():
    k = 0
    total = 0
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)

        total += num / den
        term = 2 * math.sqrt(2) / 9801 * num / den

        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / (2 * math.sqrt(2) / 9801 * total)


print(estimate_pi())
