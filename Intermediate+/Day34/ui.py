THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterFace:

	def __init__(self, quiz_brain: QuizBrain) -> None:
		# Window and Canvas
		self.quiz = quiz_brain
		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(padx=20, pady=20, bg=THEME_COLOR)

		self.canvas = Canvas(width=300, height=250, bg="white")
		self.question_text = self.canvas.create_text(150,
													125,
													width=280,
													text= "Some Question",
													fill=THEME_COLOR,
													font=("Arial", 20, "italic"))
		
		self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

		#Images
		true_image = PhotoImage(file="images/true.png")
		false_image = PhotoImage(file="images/false.png")

		#Buttons
		self.y_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
		self.y_button.grid(row=2, column=0)

		self.n_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
		self.n_button.grid(row=2, column=1)

		#Labels
		self.score_label = Label(text=f"Score: ", fg="white", bg=THEME_COLOR)
		self.score_label.grid(row= 0, column= 1)

		#Loop
		self.get_next_question()
		self.window.mainloop()

	# Methods
	def get_next_question(self):
		self.canvas.config(bg="white")
		if self.quiz.still_has_questions():
			self.score_label.config(text= f"Score: {self.quiz.score}")
			q_text = self.quiz.next_question()
			self.canvas.itemconfig(self.question_text, text=q_text)
		else:
			self.canvas.itemconfig(self.question_text, text= "You have finished the quiz!")
			self.y_button.config(state="disabled")
			self.n_button.config(state="disabled")

	def true_pressed(self):
		self.give_feedback(self.quiz.check_answer("True"))
	
	def false_pressed(self):
		self.give_feedback(self.quiz.check_answer("Flase"))

	def give_feedback(self, answer):
		if answer == True:
			self.canvas.config(bg="green")
		else:
			self.canvas.config(bg="red")
		self.window.after(1000, self.get_next_question)