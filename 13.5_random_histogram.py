import random


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def choose_from_hist(hist: dict):
    total = 0
    for freq in hist.values():
        total += freq

    index = random.randint(1, total)
    current_index = 0
    for char, freq in hist.items():
        current_index += freq
        if current_index >= index:
            return char


print(choose_from_hist(histogram("banana")))
