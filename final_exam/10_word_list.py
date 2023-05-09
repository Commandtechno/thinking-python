
def words_append():
    words = []
    for word in open("../words.txt"):
        word = word.strip()
        words.append(word)

    return words

def words_concat():
    words = []
    for word in open("../words.txt"):
        word = word.strip()
        words = words + [word]

    return words

# words_concat is slower since it has to create a new list and variable out of two lists while append just adds an element to the existing list