def has_duplicates(d):
    vals = {}
    for k in d:
        val = d[k]
        if val in vals:
            return True

        vals[val] = None

    return False


print(has_duplicates({"a": 1, "b": 2}))
print(has_duplicates({"a": 1, "b": 1}))
