def eval_loop():
    while True:
        i = input()
        if i == "done":
            break

        print(eval(i))


eval_loop()
