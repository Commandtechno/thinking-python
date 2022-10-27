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


for i in range(100_000, 1_000_000):
    if (
        is_palindrome(str(i)[-4:])
        and is_palindrome(str(i + 1)[-5:])
        and is_palindrome(str(i + 2)[2:4])
        and is_palindrome(str(i + 3))
    ):
        print(i)
