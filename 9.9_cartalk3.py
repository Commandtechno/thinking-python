def is_valid(age):
    return


diff = 36
for age in range(200):
    if str(age)[::-1] == str(age - diff).zfill(2):
        print(age)
