
import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("purple")

    brad = turtle.Turtle()
    brad.shape('circle')
    brad.color('white')
    brad.speed(2)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)
    window.exitonclick()
    
draw_square()
