from tkinter import * 
from random import *
from math import *
import datetime
# Настройки окна
root = Tk() 
root.geometry('')
root.title('Clock')
root.resizable(False, False)

width = 400
height = 400
rad = 150
canvas = Canvas(root, width=width, height=height)
canvas.pack()

canvas.create_oval(width/2-rad, height/2-rad, width/2+rad, height/2+rad)
seconds = canvas.create_line(0,0,0,0, fill='red')
minutes = canvas.create_line(0,0,0,0)
hours = canvas.create_line(0,0,0,0)

def x_coordinate(lenght, angle):
    return width/2 + lenght * cos(angle * pi / 180)
def y_coordinate(lenght, angle):
    return height/2 - lenght * sin(angle * pi / 180)

def change_hand(lenght, time, clock_hand, degree):
    alpha = 90 - time * degree
    x1 = x_coordinate(0, alpha)
    y1 = y_coordinate(0, alpha)
    x2 = x_coordinate(lenght, alpha)
    y2 = y_coordinate(lenght, alpha)
    canvas.coords(clock_hand, x1, y1, x2, y2)

def update():
    time = str(datetime.datetime.now())
    sec = int(time[17:19])
    min = int(time[14:16])
    ho = int(time[11:13])

    change_hand(rad-20, sec, seconds, 6)
    change_hand(rad - 40, min, minutes, 6)
    change_hand(rad/2, ho, hours, 30)
    root.after(1000, update)
update()

# Функции



alpha = 60
for i in range(1,13):
    canvas.create_text(x_coordinate(rad + 15, alpha), y_coordinate(rad + 15, alpha), text=i, fill='darkblue', font='Times 10 italic bold')
    alpha -= 30

for i in range(60):
    x1 = x_coordinate(rad, alpha)
    y1 = y_coordinate(rad, alpha)
    if alpha % 30 == 0:
        x2 = x_coordinate(rad - 20, alpha)
        y2 = y_coordinate(rad - 20, alpha)
    else:
        x2 = x_coordinate(rad - 10, alpha)
        y2 = y_coordinate(rad - 10, alpha)
    canvas.create_line(x1,y1,x2,y2)
    alpha += 6
# Виджеты


# Конец программы
root.mainloop()