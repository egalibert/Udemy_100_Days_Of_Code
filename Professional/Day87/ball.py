from turtle import Turtle
MOVE_SPEED = 1.5

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.shape("circle")
		self.penup()
		self.goto(0, -200)
		self.x_move = MOVE_SPEED
		self.y_move = MOVE_SPEED
		self.multiplier = 1

	def move_ball(self):
		new_x = self.xcor() + self.x_move 
		new_y = self.ycor() + self.y_move 
		self.goto(new_x, new_y)


	def bounce_y(self):
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1

	def reset_position(self):
		self.goto(0, 0)
		self.bounce_x()

	# def increase_multiplier(self):
	# 	self.multiplier += 1