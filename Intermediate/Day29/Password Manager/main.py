from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = password_letters + password_symbols + password_numbers

	shuffle(password_list)

	password = "".join(password_list)
	password_entry.insert(0, password)
	pyperclip.copy(password)
	# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	site_text = website_entry.get()
	mail_text = email_entry.get()
	pass_text = password_entry.get()

	if len(site_text) == 0 or len(pass_text) == 0:
		messagebox.showinfo(title="Oops", message= "Please don't leave any fields empty!")
	else:
		is_ok = messagebox.askokcancel(title=site_text, message=f"these are the details entered: \nEmail: {mail_text} \nPassword: {pass_text} \n Is it okay to save?")

		if is_ok:
			with open("data.txt", "a") as file:
				file.write(f"{site_text} | {mail_text} | {pass_text}\n")
			file.close()
			website_entry.delete(0, END)
			password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window and Canvas
window = Tk("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#------
#Labels

website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

#-------
#Entries

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "elliotgalibert@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#-------
#Buttons

gen_button = Button(text="Generate Password", command=password_generator)
gen_button.grid(column=2, row=3)

add_button = Button(width= 36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

#-------



window.mainloop()