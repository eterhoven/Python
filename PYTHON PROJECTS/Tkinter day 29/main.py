from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 15))
website_label.grid(column=0, row=1)
website_entry = Entry(window, width=36)
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 15))
email_label.grid(column=0, row=2)
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=(FONT_NAME, 15))
password_label.grid(column=0, row=3)
password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
