from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
	tim.forward(10)
def move_back():
	tim.backward(10)
def move_left():
	tim.left(10)
def move_right():
	tim.right(10)

def clear():
	tim.clear()
	tim.penup()
	tim.home()
	tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()