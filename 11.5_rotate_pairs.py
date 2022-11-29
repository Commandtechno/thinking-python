def rotate_word(word, num):
    rotated_word = ""
    for c in word:
        code = ord(c) + num
        if c.islower() and code < ord("a"):
            dist = ord("a") - code
            code = ord("z") - dist + 1

        if c.isupper() and code < ord("A"):
            dist = ord("A") - code
            code = ord("Z") - dist + 1

        rotated_word += chr(code)
    return rotated_word


words = {}

for word in open("words.txt"):
    words[word.strip()] = None

for word in words:
    for i in range(1, 26):
        rotated_word = rotate_word(word, i)
        if rotated_word in words:
            print(word, rotated_word)
