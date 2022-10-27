# checks if the first letter is lowercase
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# checks if "c" is lowercase, which it is, so it just returns true
def any_lowercase2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"


# returns whether the last term is lowercase
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


# actually works
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


# actually works
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
