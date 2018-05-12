import turtle

window = turtle.Screen()
window.bgcolor("#121212")

def draw_square():
    raph = turtle.Turtle()
    raph.shape('circle')
    raph.speed(2)
    raph.color('red')

    turns = 0
    while turns < 4:
        raph.forward(20)
        raph.right(90)
        turns += 1

def draw_circle():
    mike = turtle.Turtle()
    mike.shape('arrow')
    mike.speed(2)
    mike.color('orange')
    mike.circle(40)


def draw_triangle():
    don = turtle.Turtle()
    don.shape('turtle')
    don.speed(3)
    don.color('purple')

    turns = 0
    while turns < 3:
        don.forward(50)
        don.right(120)
        turns += 1
    window.exitonclick()


draw_square()
draw_circle()
draw_triangle()
