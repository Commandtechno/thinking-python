def factorial(n):
    """Computes factorial of n recursively."""
    if n <= 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(n - 1, "-", result)
        return result


factorial(int(input("Enter your age: ")))
