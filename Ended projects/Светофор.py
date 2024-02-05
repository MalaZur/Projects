from tkinter import * 
from random import *
from turtle import circle

# Настройки окна
root = Tk() 
root.geometry('300x350')
root.title(' ')
root.resizable(False, False)

# Функции


# Виджеты
canvas = Canvas(root, height=340, width=280, relief=SOLID, bg='white', bd=1)
canvas.pack()
box1 = canvas.create_rectangle(90,10, 210,290, fill='#4a4948', outline='black')
box2 = canvas.create_rectangle(100,20, 200,280, fill='grey', outline='black')
box3 = canvas.create_rectangle(140,290, 160,340, fill='#4a4948', outline='black')
circle_red = canvas.create_oval(120,40, 180,100, fill='#c70000')
circle_yellow = canvas.create_oval(120,120, 180,180, fill='#edff66')
circle_green = canvas.create_oval(120,200, 180,260, fill='#009c50')

def start():
    canvas.itemconfig(circle_red, fill='grey')
    canvas.itemconfig(circle_yellow, fill='grey')
    canvas.itemconfig(circle_green, fill='grey')
start()

def red_light(event):
    canvas.itemconfig(circle_red, fill='#c70000')
    root.after(2000, yellow_light)
def yellow_light():
    canvas.itemconfig(circle_red, fill='grey')
    canvas.itemconfig(circle_yellow, fill='#edff66')
    root.after(2000, green_light)
def green_light():
    canvas.itemconfig(circle_yellow, fill='grey')
    canvas.itemconfig(circle_green, fill='#009c50')  
    root.after(2000, start)  

    
canvas.bind_all('<space>',red_light)
# Конец программы
root.mainloop()