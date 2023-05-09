def is_abecedarian(word: str):
    sorted = list(word)
    sorted.sort()

    return "".join(sorted) == word


total = 0
for word in open("../words.txt"):
    word = word.strip()

    if is_abecedarian(word):
        print(word)
        total+=1

print("total word count:",total)