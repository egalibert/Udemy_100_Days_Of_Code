from turtle import Turtle
HEIGHT = 100
WIDTH = 20
UP = "Up"
DOWN = "Down"

class Paddle(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.shape("square")
		self.shapesize(stretch_wid=5, stretch_len=1)
		# self.turtlesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
		self.penup()
		self.goto(350, 0)
		
	def up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)
	
	def down(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)