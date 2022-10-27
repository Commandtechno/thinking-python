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


print(rotate_word("cheer", 7))
print(rotate_word("melon", -10))
print(rotate_word("IBM", -1))
