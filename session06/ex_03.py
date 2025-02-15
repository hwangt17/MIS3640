import turtle
import math

flower = turtle.Turtle()

def polyline(t, n, length, angle):
    """Draws n line segments w/ the given length and
    angle (in degrees) between them. t is a turtle.
    """    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """
    Draws a n-sided polygon w/ given length. t is a turtle.
    """
    angle = 360.0 / n
    polyline(t, n, length, angle)

def square(t, length):
    polygon(t, 4, length)

def arc(t, r, angle):
    """
    Draw a arc w/ radius r and angle. t is the turtle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t,r):
    """
    Draw a circle w/ radius r. t is the turtle.
    """
    arc(t, r, 360)

def move(t, x, y):
    """Move Turtle (t) forward (x, y) units w/out leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.setpos(x, y)
    t.pd()

