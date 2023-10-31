from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
	# time.sleep(0.1)
	screen.update()
	ball.move_ball()

	# Detect collision
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Detect collision with paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
		ball.bounce_x()

	# Detect when r_paddle misses
	if ball.xcor() > 380:
		scoreboard.l_point()
		ball.reset_position()

	# Detect when l_paddle misses
	if ball.xcor() < -380:
		scoreboard.r_point()
		ball.reset_position()

screen.exitonclick()