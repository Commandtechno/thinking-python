def recurse(n, s):
    """
    returns the sum of n and all numbers below it starting from s
    """
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)

# 1. the break condition would not execute since n would never equal 0 making it run forever
