import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Watermark App")

		self.create_widgets()

	# Create labels and buttons
	def create_widgets(self):
		self.label = tk.Label(self.root, text="Select an Image:")
		self.label.pack(pady=10)

		self.select_button = tk.Button(self.root, text="Select Image", command=self.load_image)
		self.select_button.pack(pady=10)

		self.watermark_button = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)
		self.watermark_button.pack(pady=10)


	# Open a file dialog to select an image file, display the selected image
	# Display the image in a label
	def load_image(self):
		file_path = "image.jpg"

		self.image = Image.open(file_path)
		self.image.thumbnail((300, 300))
		self.tk_image = ImageTk.PhotoImage(self.image)

		self.image_label = tk.Label(self.root, image=self.tk_image)
		self.image_label.pack(pady=10)

		self.original_image_path = file_path


	# Add a watermark (text in this example)
	def add_watermark(self):
		original_image = Image.open(self.original_image_path)

		watermark_text = "Elliot Galibert ©"
		watermark_font = ImageFont.load_default()
		draw = ImageDraw.Draw(original_image)
		draw.text((10, 10), watermark_text, font=watermark_font, fill=(255, 255, 255, 128))

		output_path = filedialog.asksaveasfilename(defaultextension=".png",
													filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
		original_image.save(output_path)

		watermarked_image = Image.open(output_path)
		watermarked_image.thumbnail((300, 300))
		tk_watermarked_image = ImageTk.PhotoImage(watermarked_image)

		watermarked_label = tk.Label(self.root, image=tk_watermarked_image)
		watermarked_label.pack(pady=10)

if __name__ == "__main__":
	root = tk.Tk()
	app = WatermarkApp(root)
	root.mainloop()