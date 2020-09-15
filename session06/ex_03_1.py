import ex_03
import turtle

petal = turtle.Turtle()
 
def flower(t): 
    for i in range(6):
        petal.lt(60)
        ex_03.arc(petal, 100, 120)
        petal.lt(60)
        ex_03.arc(petal,100,60)

flower(petal)

turtle.mainloop()
