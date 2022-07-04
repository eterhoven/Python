from cgitb import text
from tabnanny import check
from time import time
from tkinter import *
import math
from playsound import playsound as play

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

#colorhunt is good website for looking at color options

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_buttons.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    REPS += 1
        
    if REPS % 8 == 0:
        countdown_timer(LONG_BREAK_MIN)
        play('long_break.wav')
        timer_label.config(text=("Take a longer break"), fg=RED)
    elif REPS % 2 == 0:
        countdown_timer(SHORT_BREAK_MIN)
        play('short_break.wav')
        timer_label.config(text=("Take a short break"), fg=PINK)
    else:
        countdown_timer(WORK_MIN)
        play('work_start.wav')
        timer_label.config(text=("Head down"))
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown_timer(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec in range(1,10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown_timer, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            check_buttons.config(text="✔")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 45))
timer_label.config(bg=YELLOW)
timer_label.config(fg=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

start_button = Button(text="Start", command=start_timer,  highlightthickness=0)
start_button.grid(column=0, row=2)


check_buttons = Button(highlightthickness=0)
check_buttons.config(bg=YELLOW)
check_buttons.config(fg=GREEN)
check_buttons.grid(column=1, row=3)

window.mainloop()
