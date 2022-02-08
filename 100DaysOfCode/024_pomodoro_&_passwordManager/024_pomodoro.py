from tkinter import *

# For Windows users
import winsound

# ################################# CONSTANTS ##########################################################################
PINK = "#FE7171"
RED = "#FD5E53"
GREEN = "#4AA96C"
YELLOW = "#f7f5dd"
BROWN = "#BA7967"
FONT_NAME = "Helvetica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
TITLE = "timer"

reps = 0
timer = None
remaining_time = 0
timer_status = "off"


# ################################# TIMER MECHANISM ####################################################################

def start_pause():
    if timer_status in ("pause", "off"):
        start_timer()
    elif timer_status == "on":
        pause_timer()


def pause_timer():
    global timer_status

    timer_status = "pause"
    window.after_cancel(timer)
    start.config(text="START", bg=GREEN)


def start_timer():
    global reps, remaining_time, timer_status

    start.config(text="PAUSE", bg=PINK)

    if timer_status == "pause":
        timer_status = "on"
        count_down(remaining_time)
    else:
        timer_status = "on"

        reps += 1
        checkmarks.config(text=f"{int(reps / 2) * CHECKMARK}")

        if reps % 8 in (1, 3, 5, 7):
            title_label.config(text="work", fg=GREEN)
            remaining_time = WORK_MIN * 60
        elif reps % 8 == 0:
            title_label.config(text="break", fg=RED)
            remaining_time = LONG_BREAK_MIN * 60
        else:
            title_label.config(text="break", fg=PINK)
            remaining_time = SHORT_BREAK_MIN * 60
        count_down(remaining_time)


# ################################# COUNTDOWN MECHANISM ################################################################
def count_down(count):
    global timer, remaining_time
    count_min = int(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        remaining_time -= 1
        timer = window.after(1000, count_down, remaining_time)
    else:
        winsound.PlaySound("*", winsound.SND_ALIAS)
        start_timer()


# ################################# TIMER RESET ########################################################################

def reset_timer():
    global reps, timer_status
    window.after_cancel(timer)
    checkmarks.config(text="")
    title_label.config(text=TITLE)
    start.config(text="START", bg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    timer_status = "off"


# ################################# UI SETUP ###########################################################################

window = Tk()
window.title("EJ's Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Placing tomato on the screen
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=0, columnspan=3)

# Start Button
start = Button(text="START", bg=GREEN, fg="white", font=(FONT_NAME, 12, "bold"), width=11, borderwidth=0,
               command=start_pause)
start.grid(row=2, column=0)

# Reset Button
reset = Button(text="RESET", bg=BROWN, fg="white", font=(FONT_NAME, 12, "bold"), width=11, borderwidth=0,
               command=reset_timer)
reset.grid(row=2, column=2)

# Heading
title_label = Label(text=TITLE, bg=YELLOW, fg=GREEN, width=5, font=(FONT_NAME, 40, "bold"))
title_label.grid(row=0, column=1)

# Checkmarks
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 13, "bold"), wraplength=140, justify="center")
checkmarks.grid(row=3, column=0, columnspan=3)

window.mainloop()
