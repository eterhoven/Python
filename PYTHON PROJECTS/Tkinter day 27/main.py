from tkinter import *
import turtle

#window

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

#button

def button_click():
    my_label.config(text=input.get())

button = Button(text="Click me", command=button_click)
button.grid(column=1, row=1)



button = Button(text="Click me too", command=button_click)
button.grid(column=2, row=0)

#Entry

input = Entry(width=10)
input.grid(column=3, row=2)
input.get()

window.mainloop()

