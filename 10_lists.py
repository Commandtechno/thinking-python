def is_equal_list(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False

    return True


def nested_sum(l):
    total = 0
    for entry in l:
        if isinstance(entry, list):
            total += nested_sum(entry)
        else:
            total += entry

    return total


print("> nested_sum")
print(nested_sum([2, [5, 10], 3, [5, 20]]))
print()


def cumsum(l):
    total = 0
    for i in range(len(l)):
        total = l[i] = l[i] + total

    return l


print("> cumsum")
print(cumsum([1, 2, 3, 4, 5]))
print()


def middle(l):
    return l[1 : len(l) - 1]


print("> middle")
print(middle([1, 2, 3, 4, 5]))
print()


def chop(l):
    del l[0]
    del l[len(l) - 1]


print("> chop")
vegetable = [1, 2, 3, 4, 5]
chop(vegetable)
print(vegetable)
print()


def is_sorted(l):
    ol = l.copy()
    l.sort()
    return is_equal_list(ol, l)


print("> is_sorted")
print(is_sorted([1, 2, 3, 4, 5]), is_sorted([1, 2, 3, 5, 4]))
print()


def is_anagram(a, b):
    al = list(a)
    bl = list(b)
    al.sort()
    bl.sort()
    return is_equal_list(al, bl)


print("> is_anagram")
print(is_anagram("ten", "net"), is_anagram("one", "two"), is_anagram("labs", "bals"))
print()


def has_duplicates(l):
    lc = l.copy()
    lc.sort()
    last = None
    for entry in lc:
        if last == entry:
            return True

        last = entry

    return False


print("> has_duplicates")
print(has_duplicates(["a", "b", "c", "b"]), has_duplicates(["a", "d", "f"]))
print()
