
import tkinter
import math
from playsound import playsound
import threading

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    status_label.config(text=f"{"✔"*int(reps/8)}", fg=YELLOW)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        threading.Thread(target=playsound, args=("long_break.mp3",), daemon=True).start()
        timer_label.config(text="Long break!")
        status_label.config(text=f"{"✔"*int(reps/8)}", fg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        threading.Thread(target=playsound, args=("short_break.mp3",), daemon=True).start()
        timer_label.config(text="Break time!")
        count_down(short_break_sec)
    else:
        threading.Thread(target=playsound, args=("start_session.mp3",), daemon=True).start()
        timer_label.config(text="Concentrate!")
        count_down(work_sec)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    # Angela's way of time formatting
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if int(count_sec) <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min // 10}{count_min % 10}:{count_sec}")
    # My way of time formatting - worse
    #canvas.itemconfig(timer_text, text=f"{math.floor(count / 60)} :{int((count - (math.floor(count / 60) * 60))/10)}{int((count - (math.floor(count / 60) * 60))%10)}")    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
# Main window
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=50, pady=50, bg=PINK)
window.resizable(False, False)

# Tomato background
canvas = tkinter.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 14, "bold"))
canvas.grid(column=2, row=2)

# Timer
timer_label = tkinter.Label(bg=PINK, fg=YELLOW, font=(FONT_NAME, 12, "bold"), padx=0)
timer_label.grid(column=2, row=1)

# Start button
start_button = tkinter.Button(text="Start", bg=GREEN, fg=YELLOW, font=(FONT_NAME, 14, "bold"), command=start_timer)
start_button.grid(column=1, row=3)

# Reset button
reset_button = tkinter.Button(text="Reset", bg=RED, fg=YELLOW, font=(FONT_NAME, 14, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)

# Status 
status_label = tkinter.Label(text="✔", bg=PINK, fg=PINK, font=(FONT_NAME, 24, "bold"), pady=10)
status_label.grid(column=2, row=3)


window.mainloop()