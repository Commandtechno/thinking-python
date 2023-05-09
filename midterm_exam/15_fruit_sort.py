fruits = []

print("Type done once you've typed all fruits")
while True:
    fruit = input("Enter fruit: ")
    if fruit == "done":
        break

    fruits.append(fruit)

fruits.sort()
for fruit in fruits:
    print(fruit)
