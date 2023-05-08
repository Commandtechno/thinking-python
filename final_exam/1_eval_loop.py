def eval_loop():
    while True:
        code = input("> ")
        if code == "done":
            break

        print(eval(code))


eval_loop()
