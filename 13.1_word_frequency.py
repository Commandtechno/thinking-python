import string

all_words = {}

for l in open("thinkpython.txt"):
    words = l.lower()
    for c in string.punctuation:
        words = words.replace(c, "")

    for c in string.digits:
        words = words.replace(c, "")

    for word in words.split(" "):
        word = word.strip()
        if len(word) < 2:
            continue

        if word in all_words:
            all_words[word] = all_words[word] + 1
        else:
            all_words[word] = 1


def sort(x):
    return dict(sorted(x.items(), key=lambda item: item[1], reverse=True))


i = 0
for word in sort(all_words).keys():
    if i == 100:
        break

    print(word)
    i = i + 1
