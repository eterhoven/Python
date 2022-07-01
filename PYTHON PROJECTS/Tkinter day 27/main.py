from tkinter import *
import turtle

#window

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

#button

def button_click():
    my_label.config(text=input.get())

button = Button(text="Click me", command=button_click)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
input.get()

window.mainloop()

