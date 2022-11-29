words = {}

for word in open("words.txt"):
    l = list(word.strip())
    l.sort()
    key = "".join(l)
    words[key] = words.get(key, []) + [word.strip()]


def is_metathesis(a, b):
    count = 0
    for aw, bw in zip(a, b):
        if aw != bw:
            count += 1

    return count == 2


for key, anagrams in words.items():
    for a in anagrams:
        for b in anagrams:
            if a != b and is_metathesis(a, b):
                print(a, b)
