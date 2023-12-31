from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.level = 1
		self.hideturtle()
		self.penup()
		self.goto(-275, 255)
		self.write_level()

	def write_level(self):
		self.clear()
		self.write(f"Level: {self.level}", align="left", font=FONT)

	def write_game_over(self):
		# self.clear()
		self.goto(0, 0)
		self.write(f"GAME OVER", align="center", font=FONT)

