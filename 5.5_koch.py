import turtle

bob = turtle.Turtle()


def koch(t, x):
    if x < 3:
        t.fd(x)
        return
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)
    t.rt(120)
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)


def snowflake(t, x):
    for i in range(3):
        koch(t, x)
        t.rt(120)


bob.speed(0)
snowflake(bob, 200)

turtle.mainloop()
