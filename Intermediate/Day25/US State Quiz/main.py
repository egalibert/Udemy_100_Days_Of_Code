import turtle
import pandas

game_is_on = True

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

score = 0

# answer_state = screen.textinput(title=f"States correct {score}/50", prompt="What's another state's name?")
# print(answer_state)

data = pandas.read_csv("50_states.csv")
states = data["state"]
kirjasto = data.to_dict()

while game_is_on:
	answer_state = screen.textinput(title=f"States correct {score}/50", prompt="What's another state's name?")
	if answer_state == "Exit":
		break
	for state in states:
		if answer_state.lower() == state.lower():
			score += 1
			state_data = data[data.state == answer_state]
			t.goto(int(state_data.x), int(state_data.y))
			t.write(answer_state)
	if score == 50:
		break





screen.exitonclick()