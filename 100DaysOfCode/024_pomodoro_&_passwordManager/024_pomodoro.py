from tkinter import *

# For Windows users
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Helvetica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
TITLE = "timer"

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    checkmarks.config(text="")
    title_label.config(text=TITLE)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    checkmarks.config(text=f"{int(reps / 2) * CHECKMARK}")

    if reps % 8 in (1, 3, 5, 7):
        title_label.config(text= "work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps % 8 == 0:

        title_label.config(text="break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        title_label.config(text="break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        winsound.PlaySound("*", winsound.SND_ALIAS)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("EJ's Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Placing tomato on the screen
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Start Button
start = Button(text="s t a r t", bg=GREEN, font=(FONT_NAME, 10), borderwidth=0, command=start_timer)
start.grid(row=2, column=0)
start.config(padx=5)

# Reset Button
reset = Button(text="r e s e t", bg=PINK, font=(FONT_NAME, 10), borderwidth=0, command=reset_timer)
reset.grid(row=2, column=2)
reset.config(padx=5)

# Heading
title_label = Label(text=TITLE, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)

# Checkmarks
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 13, "bold"))
checkmarks.grid(row=3, column=1)

window.mainloop()
