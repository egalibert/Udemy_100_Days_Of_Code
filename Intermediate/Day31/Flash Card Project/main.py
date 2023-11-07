BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

from tkinter import *
import random
import pandas

# Read data
try:
	data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	orginal_data = pandas.read_csv("data/french_words.csv")
	to_learn = orginal_data.to_dict(orient="records")
else:
	to_learn = data.to_dict(orient="records")

#-----------
#Functions
def next_card():
	global current_card, flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(to_learn)

	# current_card["French"]
	canvas.itemconfig(card_title, text="French", fill="Black")
	canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
	canvas.itemconfig(canvas_image, image=front_image)
	flip_timer = window.after(3000, flip_card)

def flip_card():
	global current_card
	canvas.itemconfig(card_title, text="English", fill="White")
	canvas.itemconfig(card_word, text=current_card["English"], fill="White")
	canvas.itemconfig(canvas_image, image=back_image)

def is_known():
	to_learn.remove(current_card)
	data = pandas.DataFrame(to_learn)
	data.to_csv("data/words_to_learn.csv", index=False)


#--------------
# Window and canvas
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, flip_card)

canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
front_image = flash_card_front = PhotoImage(file="images/card_front.png")
back_image = flash_card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=flash_card_front)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

#-------------
# Images
my_image_g = PhotoImage(file="images/right.png")
my_image_r = PhotoImage(file="images/wrong.png")

#-------------
# Buttons
yes_button = Button(image=my_image_g, highlightthickness=0, command=next_card)
yes_button.grid(row=1, column=0)
no_button = Button(image=my_image_r, highlightthickness=0, command=next_card)
no_button.grid(row=1, column=1)

#-------------

next_card()
flip_card()

window.mainloop()