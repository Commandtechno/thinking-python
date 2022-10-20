import math
from turtle import Turtle
import turtle


def hypotenuse(a: int, b: int):
    return math.sqrt(a * a + b * b)


def draw_a(t: Turtle):
    t.lt(90)
    t.fd(120)
    t.rt(90)
    t.fd(60)
    t.rt(90)
    t.fd(60)
    t.rt(90)
    t.fd(60)
    t.rt(180)
    t.fd(60)
    t.rt(90)
    t.fd(60)
    t.lt(90)


def draw_k(t: Turtle):
    t.lt(90)
    t.fd(120)
    t.rt(180)
    t.fd(60)
    t.lt(135)
    t.fd(hypotenuse(60, 60))
    t.rt(180)
    t.fd(hypotenuse(60, 60))
    t.lt(90)
    t.fd(hypotenuse(60, 60))
    t.lt(45)


def draw_h(t: Turtle):
    t.lt(90)
    t.fd(120)
    t.rt(180)
    t.fd(60)
    t.lt(90)
    t.fd(60)
    t.lt(90)
    t.fd(60)
    t.lt(180)
    t.fd(120)
    t.lt(90)


def draw_i(t: Turtle):
    t.fd(30)
    t.lt(90)
    t.fd(120)
    t.lt(90)
    t.fd(30)
    t.lt(180)
    t.fd(60)
    t.lt(180)
    t.fd(30)
    t.lt(90)
    t.fd(120)
    t.lt(90)
    t.fd(30)


def draw_l(t: Turtle):
    t.lt(90)
    t.fd(120)
    t.lt(180)
    t.fd(120)
    t.lt(90)
    t.fd(60)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

draw_a(bob)
move(bob, 30)
draw_k(bob)
move(bob, 30)
draw_h(bob)
move(bob, 30)
draw_i(bob)
move(bob, 30)
draw_l(bob)


turtle.mainloop()
