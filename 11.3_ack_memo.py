def ack(m, n):
    if m == 0:
        return n + 1

    if m > 0 and n == 0:
        return ack(m - 1, 1)

    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


def memo(f):
    cache = {}

    def memoized(*args):
        if args in cache:
            print("cached")
            return cache[args]

        res = f(*args)
        cache[args] = res

        return res

    return memoized


memoized_ack = memo(ack)
print(memoized_ack(3, 4))
print(memoized_ack(3, 5))
print(memoized_ack(3, 4))
print(memoized_ack(3, 5))
