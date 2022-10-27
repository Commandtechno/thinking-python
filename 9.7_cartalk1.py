f = open("words.txt")


for word in f:
    word = word.strip()

    i = 0
    while i < len(word) - 5:
        if (
            word[i] == word[i + 1]
            and word[i + 2] == word[i + 3]
            and word[i + 4] == word[i + 5]
        ):
            print(word)
            break

        i += 1
