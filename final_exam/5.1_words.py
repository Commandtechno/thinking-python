f = open("../words.txt")


first_name = input("What is your first name? ")
day_of_birth = int(input("What is your day of birth? "))

word_count = -1
new_words = open("new_words.txt", "w")
for word in f:
    word = word.strip()

    if word[0] == first_name[0]:
        word_count = 0

    if word_count >= 0:
        new_words.write(word + "\n")

    if word_count >= day_of_birth * 4:
        break
