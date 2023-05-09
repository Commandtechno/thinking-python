words = []
for word in open("../words.txt"):
    word = word.strip()
    words.append(word)

open("words_original.txt", "w").write("\n".join(words))

words.sort()

open("words_sorted_asc.txt", "w").write("\n".join(words))

words.reverse()

open("words_sorted_desc.txt", "w").write("\n".join(words))
