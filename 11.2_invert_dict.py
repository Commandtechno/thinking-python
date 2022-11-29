def invert_dict(d):
    i = {}
    for k in d:
        v = d[k]
        i.setdefault(v, []).append(k)

    return i


print(invert_dict({"a": 1, "b": 2, "c": 3, "d": 2}))
