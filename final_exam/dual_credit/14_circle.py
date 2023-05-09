import turtle
import math

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

def polyline(t, n, length, angle):
    print("drawing line with", n, "segments,", "length:", length, "and angle", angle)
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    print("drawing arc with radius:", r, "and angle:", angle)
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def draw_circle(t, c: Circle):
    bob.penup()
    bob.goto(c.center.x, c.center.y)
    bob.pendown()
    bob.dot()
    bob.penup()
    bob.goto(c.center.x, c.center.y - c.radius)
    bob.pendown()
    arc(bob, c.radius, 360)

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist


def point_in_rect(r, p):
    return (
        r.corner.x <= p.x <= r.corner.x + r.width
        and r.corner.y <= p.y <= r.corner.y + r.height
    )


def point_in_circle(c, p):
    return distance_between_points(c.center, p) <= c.radius


def rect_in_circle(c, r):
    return distance_between_points(c.center, r.corner) <= c.radius

c = Circle()
c.center = Point()
c.center.x = 150
c.center.y = 150
c.radius = 75

p = Point()
p.x = 100
p.y = 100

r = Rect()
r.corner = Point()
r.corner.x = 50
r.corner.y = 50
r.width = 100
r.height = 100

print(point_in_rect(r, p))
print(rect_in_circle(c, r))

bob = turtle.Turtle()
draw_circle(bob, c)

turtle.mainloop()