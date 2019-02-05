import turtle
import math

# square bob
# bob = turtle.Turtle()
# print(bob)

# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.rt(90)
# bob.bk(100)
# bob.rt(90)
# bob.fd(100)
# bob.pu()

# for i in range(4):
#   print('Hello!')

# for i in range(4):
#   bob.fd(100)
#   bob.lt(90)

# turtle.mainloop()

## =========== 4.3 EXERCISES ===========

# def square(t, length):
#   for i in range(4):
#     t.fd(length)
#     t.lt(90)
#   turtle.mainloop()

# square(bob, 200)

# def polygon(t, n, length):
#   angle = 360/n
#   for i in range(n):
#     t.fd(length)
#     t.lt(angle)
#   turtle.mainloop()

# polygon(bob, 100, 5)
# polygon(bob, 100, 6)
# polygon(bob, 100, 10)
# polygon(bob, length=10, n=20)

# length will have to be smaller gradually
# n will need to grow higher

# def circle(t, r):
#   circumference = 2 * math.pi * r
#   n = 50
#   length = circumference / n
#   polygon(t, length, n)

# circle(bob, 100)

# def polyline(t, n, length, angle):
#     """Draws n line segments with the given length and
#     angle (in degrees) between them.  t is a turtle.
#     """    
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# def polygon(t, n, length):
#     angle = 360.0 / n
#     polyline(t, n, length, angle)

# # transform polygon into an arc
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     print('arc_length', arc_length)
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, step_length, step_angle)

# #refactor polygon to be polyline, you have bob the turtle, n=sides, length, and angle
# def circle(t, r):
#     arc(t, r, 360)

# circle(bob, 50)

# # make sure preconditions and postconditions are well defined!

## ======== EXERCISES ========
def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
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
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # wait for the user to close the window
    turtle.mainloop()