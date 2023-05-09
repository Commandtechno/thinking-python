word = input("Enter word: ")

if not word:
    print("Invalid input")
else:
    z = int(input("Enter how many times to reverse the string: "))
    for i in range(z):
        word = word[::-1]
        print(word)
