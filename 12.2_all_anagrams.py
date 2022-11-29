words = {}

for word in open("words.txt"):
    l = list(word.strip())
    l.sort()
    key = "".join(l)
    words[key] = words.get(key, []) + [word.strip()]

print("- all anagrams")
for key, anagrams in words.items():
    if len(anagrams) > 1:
        print(anagrams)

longest = []
for key, anagrams in words.items():
    if len(key) == 8 and len(anagrams) > len(longest):
        longest = anagrams

print()
print("- longest scrabble bingo")
print(longest)
