from turtle import Screen, Turtle
from paddle import Paddle
WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
	screen.update()


screen.exitonclick()