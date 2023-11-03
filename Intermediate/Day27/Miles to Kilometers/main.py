from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column= 1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column= 2, row= 0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column = 0, row= 1)

kilometer_result_ladel = Label(text="0")
kilometer_result_ladel.grid(column= 1, row= 1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column= 2, row= 1)

def button_clicked():
	kilometer_result_ladel["text"] = str(int(miles_input.get()) * 1.609344)

button = Button(text='Convert', command=button_clicked)
button.grid(column= 1, row= 2)





window.mainloop()