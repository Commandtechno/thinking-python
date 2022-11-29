def most_frequent(word):
    chars = {}
    for char in word.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return sort(chars)


def sort(x):
    return dict(sorted(x.items(), key=lambda item: item[1], reverse=True))


print(most_frequent("mississippi"))
