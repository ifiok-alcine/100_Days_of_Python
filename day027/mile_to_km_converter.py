from tkinter import *


def calculate():
    number = miles_input.get()
    km_convert = float(number) * 1.609
    km_answer_label.config(text=km_convert)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Ariel", 10))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal", font=("Ariel", 10))
is_equal_label.grid(column=0, row=1)

km_answer_label = Label(text="0", font=("Ariel", 10))
km_answer_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Ariel", 10))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

mainloop()
