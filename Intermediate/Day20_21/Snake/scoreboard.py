from turtle import Turtle
ALINGMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("White")
		self.hideturtle()
		self.penup()
		self.goto(0, 270)
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(arg=f"Score: {self.score}", align=ALINGMENT, font=FONT)

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)
		self.write(arg=f"GAME OVER", align=ALINGMENT, font=FONT)