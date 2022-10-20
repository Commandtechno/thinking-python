def gcd(a, b):
    for i in range(b):
        n = b - i
        if a % n == 0 and b % n == 0:
            return n


print(gcd(12, 16))
