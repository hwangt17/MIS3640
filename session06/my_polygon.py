import turtle

leo = turtle.Turtle()

leo.fd(100)
leo.lt(90)
leo.fd(100)
leo.lt(90)
leo.fd(100)
leo.lt(90)
leo.fd(100)

#exercise 2.1
def square(t): 
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(leo)

#exercise 2.2
raphael = turtle.Turtle()

def square(t, length): 
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(raphael, 100)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle.
    """    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#exercise 2.3
bob = turtle.Turtle()

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)
    
polygon(bob,7,70)

#exercise 2.4
import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

arc(bob, 100, 180)

def circle(t, r):
    arc(t, r, 360)

circle(bob, 10)

print(leo) 
"""This tells us that leo refers to an object with 
type Turtle as defined in module turtle."""

turtle.mainloop()

