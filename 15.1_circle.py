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


def make_point(x, y):
    p = Point()
    p.x = x
    p.y = y


def circle_rect_overlap(c, r):
    return (
        point_in_circle(c, r.corner)
        or point_in_circle(c, make_point(r.corner.x + r.width, r.corner.y))
        or point_in_circle(c, make_point(r.corner.x, r.corner.y + r.height))
        or point_in_circle(r.corner.x + r.width, r.corner.y + r.height)
    )


p = Point()
p.x = 100
p.y = 100

r = Rect()
r.corner = Point()
r.corner.x = 50
r.corner.y = 50
r.width = 100
r.height = 100

c = Circle()
c.center = Point()
c.center.x = 100
c.center.y = 100
c.radius = 100

print(point_in_rect(r, p))
print(rect_in_circle(c, r))
print(circle_rect_overlap(c, r))
