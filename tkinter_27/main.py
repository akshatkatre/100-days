from tkinter import *


def button_clicked():
    user_input = int(input_field.get())
    print(user_input)
    my_label.config(text = f"is equal to {user_input * 1.6}  km")


window = Tk()
window.title('Miles to Km converter')
window.minsize(width=300, height=200)

input_field = Entry(width=10)
input_field.pack()

my_label = Label(font=("Ariel", 16))
my_label.pack()

button = Button(text="Calculate", command=button_clicked)
button.pack()


window.mainloop()
