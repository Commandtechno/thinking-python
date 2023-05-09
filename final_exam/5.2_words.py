f = open("../words.txt")

for word in f:
    word = word.strip()

    if len(word) > 12:
        print(word)
