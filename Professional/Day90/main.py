import tkinter as tk
from datetime import datetime

class TypingSpeedApp:
	def __init__(self, root):
		self.root = root
		self.root.title("The Most Dangerous Writing App")
		self.sample_text = "Write something, and if you stop for 5 seconds, your progress will be lost."

		self.user_input = tk.StringVar()
		self.last_input_time = None
		self.timeout_interval = 5000  # Timeout interval in milliseconds (e.g., 5 seconds)
		self.flash_duration = 500  # Flash duration in milliseconds

		self.create_widgets()

	def create_widgets(self):
		self.sample_text_widget = tk.Text(self.root, wrap="word", height=2, state="disabled")
		self.sample_text_widget.pack(pady=15)
		self.sample_text_widget.insert(tk.END, self.sample_text)

		self.text_entry_label = tk.Label(self.root, text="Start typing:")
		self.text_entry_label.pack()

		self.text_entry = tk.Entry(self.root, textvariable=self.user_input, width=60)
		self.text_entry.pack(pady=15)

		self.start_button = tk.Button(self.root, text="Start Typing", command=self.start_typing_test)
		self.start_button.pack()

		self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_typing_test, state="disabled")
		self.reset_button.pack()

	def start_typing_test(self):
		self.sample_text_widget.config(state="normal")
		self.sample_text_widget.delete(1.0, tk.END)
		self.sample_text_widget.insert(tk.END, self.sample_text)
		self.sample_text_widget.config(state="disabled")

		self.user_input.set("")  # Clear the user input
		self.text_entry.bind("<Key>", self.on_key_pressed)
		self.last_input_time = datetime.now()
		self.start_button.config(state="disabled")
		self.reset_button.config(state="normal")
		self.check_input_timeout()

	def on_key_pressed(self, event):
		self.last_input_time = datetime.now()

	def check_input_timeout(self):
		current_time = datetime.now()
		elapsed_time = (current_time - self.last_input_time).total_seconds() * 1000  # Convert to milliseconds

		if elapsed_time > self.timeout_interval:
			# User has not typed anything for the specified interval
			self.reset_typing_test()
			self.flash_background()
		else:
			# Schedule the function to run again after a short interval
			self.root.after(100, self.check_input_timeout)

	def flash_background(self):
		original_bg_color = self.root.cget("bg")
		self.root.configure(bg="red")
		self.root.after(self.flash_duration, lambda: self.root.configure(bg=original_bg_color))

	def reset_typing_test(self):
		self.start_button.config(state="normal")
		self.reset_button.config(state="disabled")
		self.sample_text_widget.config(state="normal")
		self.sample_text_widget.delete(1.0, tk.END)
		self.sample_text_widget.config(state="disabled")

		self.user_input.set("")  # Clear the text entry

if __name__ == "__main__":
	root = tk.Tk()
	app = TypingSpeedApp(root)
	root.mainloop()



