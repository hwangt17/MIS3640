import ex_03
import turtle
import math

frank = turtle.Turtle()

triangle_length = 100

half_triangle_length = triangle_length/2

def triangle(t):
    for i in range(3):
        frank.lt(60)
        frank.fd(triangle_length)
        frank.lt(60)

def all_triangles(t):
    for i in range(4):
        triangle(frank)
        frank.lt(90)

def small_circles(t):
    ex_03.circle(frank, half_triangle_length/math.sqrt(3))

all_triangles(frank)
ex_03.move(frank, 0, half_triangle_length/math.sqrt(3))
small_circles(frank)
ex_03.move(frank, 0, -half_triangle_length*3/math.sqrt(3))
small_circles(frank)
ex_03.move(frank, half_triangle_length*2/math.sqrt(3), -half_triangle_length/math.sqrt(3))
small_circles(frank)
ex_03.move(frank, -half_triangle_length*2/math.sqrt(3), -half_triangle_length/math.sqrt(3))
small_circles(frank)
ex_03.move(frank, 0, -triangle_length)
ex_03.circle(frank, triangle_length)

turtle.mainloop()