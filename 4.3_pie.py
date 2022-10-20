import math
import turtle

bob = turtle.Turtle()


def isosceles(t, r, angle):
    """Draws an icosceles triangle.
    The turtle starts and ends at the peak, facing the middle of the base.
    t: Turtle
    r: length of the equal legs
    angle: half peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90 + angle)
    t.fd(2 * y)
    t.lt(90 + angle)
    t.fd(r)
    t.lt(180 - angle)


def poly(t, r, sides):
    for i in range(sides):
        isosceles(t, r, 180 / sides)
        bob.right(360 / sides)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


move(bob, -200)
poly(bob, 100, 3)
move(bob, 200)
poly(bob, 100, 4)
move(bob, 200)
poly(bob, 100, 5)


turtle.mainloop()
