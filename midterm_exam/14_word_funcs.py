def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) < 2:
        return True

    return first(word) == last(word) and is_palindrome(middle(word))


print(is_palindrome(input("Enter word: ")))
