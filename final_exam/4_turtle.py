import turtle


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


bob = turtle.Turtle()
square(bob, 10)
square(bob, 20)
square(bob, 30)

turtle.mainloop()
