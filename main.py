PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.10
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.05
reps=0
timer=None
from tkinter import *
import math

def resettimer():
    window.after_cancel(timer)
    global reps
    reps=0
    check.config(text="")
    title.config(text="Timer", fg=RED)
    canvas.itemconfig(time,text="00:00")



def starttimer():
    global reps
    reps+=1
    if reps%8==0:
        title.config(text="Break",fg=RED)
        countdown(LONG_BREAK_MIN*60)
    elif reps%2==0:
        title.config(text="Break",fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    else:
        title.config(text="Work")
        countdown(WORK_MIN*60)

def countdown(count):
    minutes=math.floor(count/60)
    seconds=int(count%60)
    if seconds<10:
        seconds=f"0{seconds}"
    canvas.itemconfig(time,text=f"{minutes}:{seconds}")

    if count>0:
        global timer
        timer=window.after(1000, countdown,count - 1)
    else:
        starttimer()
        checks=""
        for i in range(math.floor(reps/2)):
           checks+="✔️"
        check.config(text=checks)

window=Tk()
window.title("PODOMORO")
window.configure(bg=YELLOW,padx=50,pady=50)

title=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,25,"bold"))
title.grid(row=0,column=1)

canvas=Canvas(height=224,width=200,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
time=canvas.create_text(100,125,text="00:00",font=(FONT_NAME,25,"bold"))
canvas.grid(row=1,column=1)

start=Button(text="start",font=(FONT_NAME,10,"bold"),command=starttimer)
reset=Button(text="reset",font=(FONT_NAME,10,"bold"),command=resettimer)
start.grid(row=2,column=0,)
reset.grid(row=2,column=2,)

check=Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))
check.grid(row=3,column=1)



window.mainloop()