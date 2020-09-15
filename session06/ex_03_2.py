import ex_03
import turtle

carl = turtle.Turtle()

#half circles
def yin_yang(t):
    for i in range(2):
        ex_03.move(carl, 0, 0)
        ex_03.arc(carl, 100, 180)

#small circles
def small_circle(t):
    ex_03.move(carl, 0, 75)
    ex_03.circle(carl, 25)
    ex_03.move(carl, 0, -125)
    ex_03.circle(carl, 25)


yin_yang(carl)
ex_03.circle(carl, 200)
small_circle(carl)

turtle.mainloop()
