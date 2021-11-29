from tkinter import *
import math

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


# ---------------------------- Start Program ------------------------------- #
def play_pomidoro():
    change_button()
    start_timer()

# ---------------------------- Change button ------------------------------- #
def change_button():
    if left_botton['state'] == "normal":
        left_botton.config(state="disable")
        right_botton.config(state="normal")
    else:
        left_botton.config(state="normal")
        right_botton.config(state='disable')

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    REPS = 0
    change_button()
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text='Timer', fg=GREEN)
    mark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_breack_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        countdown(short_breack_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Working", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    reformat_count_minutes = math.floor(count / 60)
    reformat_count_secundes = count % 60

    if reformat_count_secundes == 0:
        reformat_count_secundes = "00"

    if int(reformat_count_secundes) < 10 and int(reformat_count_secundes) != 0:
        reformat_count_secundes_part2 = reformat_count_secundes
        reformat_count_secundes = f"0{reformat_count_secundes_part2}"

    canvas.itemconfig(timer_text, text=f"{reformat_count_minutes}:{reformat_count_secundes}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(REPS / 2)
        for _ in range(work_session):
            mark += '✔'
        mark_label.config(text=f"{mark}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomidoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo)

timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

mark_label = Label(font=(FONT_NAME, 10, 'bold'), fg=GREEN, bg=YELLOW)
mark_label.grid(column=1, row=4)

left_botton = Button(text='Start', font=(FONT_NAME, 9, 'bold'), relief='raised', highlightthickness=0,
                     command=play_pomidoro)
left_botton.grid(column=0, row=3)

right_botton = Button(text='Reset', font=(FONT_NAME, 9, 'bold'), relief='raised', highlightthickness=0,
                      command=reset_timer, state="disable")

right_botton.grid(column=3, row=3)

window.mainloop()
