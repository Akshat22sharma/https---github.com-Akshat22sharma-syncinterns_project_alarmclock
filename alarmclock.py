from tkinter import *
import datetime
import time
import winsound

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

def alarm():
    while True:
        set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        time.sleep(1)
 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
 
        if current_time == set_alarm:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x400")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="white",bg="black",font=("Helevetica",7,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "white",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "white",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 15).place(x=200,y=30)

submit = Button(clock,text = "Set Alarm",fg="white", bg="black",width = 10,command = actual_time).place(x =110,y=70)
 
clock.mainloop()

