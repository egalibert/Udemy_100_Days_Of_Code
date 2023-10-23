from turtle import Turtle, Screen
import random
TK_SILENCE_DEPRECATION=1

# EX1, Draw a square
timmy_the_turtle = Turtle()

for _ in range(4):
	timmy_the_turtle.forward(100)
	timmy_the_turtle.left(90)

# EX2, Draw a dashed line

for _ in range(20):
	timmy_the_turtle.forward(12)
	timmy_the_turtle.penup()
	timmy_the_turtle.forward(10)
	timmy_the_turtle.pendown()


# EX3 draw multiple shapes

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
	angle = 360 / num_sides
	for _ in range(num_sides):
		timmy_the_turtle.forward(100)
		timmy_the_turtle.right(angle)

for shape_side_n in range(3, 10):
	timmy_the_turtle.color(random.choice(colours))
	draw_shape(shape_side_n)


# EX4 draw a random walk

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(200):
	timmy_the_turtle.color(random.choice(colours))
	timmy_the_turtle.forward(30)
	timmy_the_turtle.setheading(random.choice(directions))

# EX5 draw a spirograph

tim = Turtle()
tim.colormode(255)
def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color

def draw_spirograph(size_of_gap):
	for _ in range(int(360 / size_of_gap)):
		tim.color(random_color())
		tim.circle(100)
		tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)










