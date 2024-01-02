from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball


import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

#Wall of blocks

blocks = []

num_blocks = 10
block_height = 20
block_width = 100
gap = 8

for row in range(num_blocks):
	for col in range(num_blocks):
		block = Turtle()
		block.shape("square")
		block.color("blue")
		block.shapesize(stretch_wid=1, stretch_len=4)  # Adjust the size as needed
		block.penup()
		x_cor = -((num_blocks - 1) * block_width + gap) / 2 + col * (block_width + gap)
		y_cor = 200 - row * (block_height + gap)
		block.goto(x_cor, y_cor)
		blocks.append(block)


paddle = Paddle(0, -250)
ball = Ball()

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

game_is_on = True
while game_is_on:
	# time.sleep(0.1)
	screen.update()
	ball.move_ball()

	# Detect collision with paddle
	if ball.ycor() > 280 or ball.distance(paddle) < 30 and ball.ycor() < -250:
		ball.bounce_y()

	# Detect collision with sidewalls
	if ball.xcor() > 380 or ball.xcor() < -380:
		ball.bounce_x()

	for block in blocks:
		if ball.distance(block) < 30:  # Adjust the collision distance as needed
			blocks.remove(block)
			block.hideturtle()  # Hide the block
			ball.bounce_y()

	# Detect when paddle misses
	if ball.ycor() < -300:
		# ball.increase_multiplier()
		ball.reset_position()

screen.exitonclick()