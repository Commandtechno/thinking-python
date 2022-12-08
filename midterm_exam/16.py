import random


def roll(x):
    return random.randint(1, x)


x = int(input("Enter amount of sides: "))
y = int(input("Enter amount of rolls: "))

results = []

for i in range(y):
    results.append(roll(x))

results.sort()

for result in results:
    print(result)
