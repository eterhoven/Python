from tkinter import *

#window

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Label is equal to

equal_label = Label(text="is equal to", font=("Arial", 24))
equal_label.grid(column=0, row=1)

#Label Miles

miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)

#Label Km

km_label = Label(text="Km", font=("Arial", 24))
km_label.grid(column=2, row=1)

#Label output

output_label = Label(text="0", font=("Arial", 24))
output_label.grid(column=1, row=1)

#Entry

input = Entry(width=20)
input.grid(column=1, row=0)
enquiry = input.get()

#button

def button_click():
    number = int(input.get())
    answer = float(number*1.6)
    output_label.config(text=round(answer, 2))

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

window.mainloop()
