from turtle import Turtle
HEIGHT = 20
WIDTH = 100

# UP = "Up"
# DOWN = "Down"

class Paddle(Turtle):

	def __init__(self, x_position, y_position):
		super().__init__()
		self.color("white")
		self.shape("square")
		self.shapesize(stretch_wid=1, stretch_len=5)
		# self.turtlesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
		self.penup()
		self.goto(x_position, y_position)
		
	def left(self):
		new_x = self.xcor() - 20
		self.goto(new_x, self.ycor())
	
	def right(self):
		new_x = self.xcor() + 20
		self.goto(new_x, self.ycor())