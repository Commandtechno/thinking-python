words = {}

for word in open("words.txt"):
    words[word.strip()] = None

print("aaa" in words)
