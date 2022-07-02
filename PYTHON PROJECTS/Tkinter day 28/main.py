from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#colorhunt is good website for looking at color options

# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 38))
timer_label.config(bg=YELLOW)
timer_label.config(fg=GREEN)
timer_label.pack()

canvas = Canvas(width=300, height=336, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(140, 112, image=tomato_img)
canvas.create_text(140, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

reset_button = Button(text="Reset", borderwidth=0)
reset_button.place(x=240, y=290)

start_button = Button(text="Start", borderwidth=0)
start_button.place(x=-20, y=290)

check_button = Button(text="√", borderwidth=0)
check_button.place(x=120, y=290)

window.mainloop()
