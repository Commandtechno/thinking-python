import turtle


class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """


class Rect:
    """Represents a rectangle.
    attributes: width, height, corner.
    """


class Circle:
    """Represents a circle.
    attributes: center, radius
    """


def draw_rect(t: turtle.Turtle, r):
    t.goto([r.corner.x, r.corner.y])
    t.fd(r.width)
    t.lt(90)
    t.fd(r.height)
    t.lt(90)
    t.fd(r.width)
    t.lt(90)
    t.fd(r.height)
    t.lt(90)


bob = turtle.Turtle()

r = Rect()
r.corner = Point()
r.corner.x = 50
r.corner.y = 50
r.width = 100
r.height = 100
draw_rect(bob, r)


turtle.mainloop()
