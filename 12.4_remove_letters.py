words = {"a": None, "i": None}
cache = {}

for word in open("words.txt"):
    words[word.strip().lower()] = None


def r(word, stack):
    if word in cache:
        print(cache[word])

    for i in range(len(word)):
        removed = word[:i] + word[i + 1 :]
        if removed in words:
            new_stack = stack + [removed]
            if len(removed) == 1:
                cache[word] = new_stack
                print(new_stack)
            else:
                r(removed, new_stack)


for word, _ in words.items():
    r(word, [word])
