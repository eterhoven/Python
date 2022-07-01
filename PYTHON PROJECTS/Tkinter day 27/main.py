from re import T
import tkinter
import turtle

#window

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

tim = turtle.Turtle()
tim.write("Some text", font=("Time New Roman", 80, "bold"))





window.mainloop()

