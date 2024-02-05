from tkinter import * 
from random import *

# Настройки окна
root = Tk() 
root.geometry('320x320')
root.title(' ')
root.resizable(False, False)

canvas = Canvas(root, height=300, width=300, relief=SOLID, bd=1, bg='white')
canvas.pack()

body_black = canvas.create_oval(60,80, 260, 280, fill='black')
body_gray = canvas.create_oval(80,140, 240,270, fill='gray', outline='gray')
body_white = canvas.create_oval(100,140, 220,270, fill='white', outline='white')

eye_left = canvas.create_oval(120,90, 157,130, fill='white', outline='white')
eyeball_left = canvas.create_oval(135,105, 150, 120, fill='black')
eye_right = canvas.create_oval(163,95, 210,130, fill='white', outline='white')
eyeball_right = canvas.create_oval(167,109, 176, 117, fill='black')

foot_left = canvas.create_oval(75,252, 158, 290, fill='yellow')
foot_right = canvas.create_oval(75+85,252, 158+85, 290, fill='yellow')

beak = canvas.create_polygon(130,140,190,140,160,180, fill='#f2c80c', outline='#f2c80c')
wing_left = canvas.create_polygon(20,170, 70,170, 70, 140, fill='black')
wing_right = canvas.create_polygon(250,170, 300,170, 250, 140, fill='black')

blink_left = canvas.create_rectangle(120, 112, 158, 120, fill='white', state=HIDDEN)
blink_right = canvas.create_rectangle(162, 112, 200, 120, fill='white', state=HIDDEN)

def do_steps(event):
    key = event.keysym
    if key == 'Left':
        canvas.move(foot_left,0, -5)
        canvas.move(foot_right, 0 , 5)
        canvas.move(wing_left, 0 , 5)
        canvas.move(wing_right, 0, -5)
    elif key == 'Right':
        canvas.move(foot_right, 0 , -5)
        canvas.move(foot_left,0, 5)
        canvas.move(wing_left, 0 , -5)
        canvas.move(wing_right, 0, 5)

def blink(event):
    canvas.itemconfig(eye_left, state=HIDDEN)
    canvas.itemconfig(eyeball_left, state=HIDDEN)
    canvas.itemconfig(eye_right, state=HIDDEN)
    canvas.itemconfig(eyeball_right, state=HIDDEN)
    canvas.itemconfig(blink_left, state=NORMAL)
    canvas.itemconfig(blink_right, state=NORMAL)

def unblink(event):
    canvas.itemconfig(eye_left, state=NORMAL)
    canvas.itemconfig(eyeball_left, state=NORMAL)
    canvas.itemconfig(eye_right, state=NORMAL)
    canvas.itemconfig(eyeball_right, state=NORMAL)
    canvas.itemconfig(blink_left, state=HIDDEN)
    canvas.itemconfig(blink_right, state=HIDDEN)

canvas.bind_all('<Key>', do_steps)
canvas.bind_all('<KeyPress-a>', blink)
canvas.bind_all('<KeyPress-z>', unblink)
# Конец программы
root.mainloop()