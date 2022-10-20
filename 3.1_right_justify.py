def right_justify(v):
    while len(v) < 70:
        v = " " + v
    return v


print(right_justify("aaaaaaaaaaaaa"))
