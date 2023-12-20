import tkinter as tk
from datetime import datetime
import random
from words import random_words

class TypingSpeedApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Typing Speed Test")
		self.sample_text = " ".join(random.sample(random_words, 20))

		self.current_text_index = 0
		self.user_input = tk.StringVar()
		self.start_time = None

		self.create_widgets()

	def create_widgets(self):
		self.sample_text_widget = tk.Text(self.root, wrap="word", height=2, state="disabled")
		self.sample_text_widget.pack(pady=15)
		self.sample_text_widget.insert(tk.END, self.sample_text)

		self.text_entry_label = tk.Label(self.root, text="Type the above text:")
		self.text_entry_label.pack()

		self.text_entry = tk.Entry(self.root, textvariable=self.user_input, width=60)
		self.text_entry.pack(pady=15)

		self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test)
		self.start_button.pack()

		self.result_label = tk.Label(self.root, text="")
		self.result_label.pack(pady=15)

	def start_typing_test(self):
		self.start_time = datetime.now()
		self.current_text_index = 0
		self.update_sample_text_widget()
		self.text_entry.delete(0, tk.END)
		self.text_entry.bind("<Key>", self.check_input)

	def update_sample_text_widget(self):
		highlighted_text = self.sample_text[:self.current_text_index]
		remaining_text = self.sample_text[self.current_text_index:]

		self.sample_text_widget.config(state="normal")
		self.sample_text_widget.delete(1.0, tk.END)
		self.sample_text_widget.insert(tk.END, highlighted_text, "correct")
		self.sample_text_widget.insert(tk.END, remaining_text)
		self.sample_text_widget.tag_configure("correct", foreground="green")
		self.sample_text_widget.config(state="disabled")

	def check_input(self, event):
		entered_text = self.user_input.get()

		# Compare the entered text with the sample text
		if entered_text == self.sample_text:
			self.end_typing_test()
			self.text_entry.delete(0, tk.END)  # Clear the input field

		# Update the display
		self.update_sample_text_widget()

	
	def clear_input_after_delay(self):
		self.text_entry.delete(0, tk.END)


	def end_typing_test(self):
		end_time = datetime.now()
		elapsed_time = (end_time - self.start_time).total_seconds() / 60.0
		words_typed = len(self.sample_text.split())
		wpm = int(words_typed / elapsed_time)

		result_text = f"Typing test completed!\nWords per minute: {wpm}"
		self.result_label.config(text=result_text)
		self.text_entry.unbind("<Key>")

if __name__ == "__main__":
	root = tk.Tk()
	app = TypingSpeedApp(root)
	root.mainloop()