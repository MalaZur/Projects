from tkinter import * 
from random import *
from turtle import bgcolor

# Настройки окна
root = Tk() 
root.geometry('450x450')
root.title(' ')
root.resizable(False, False)

canvas = Canvas(height=450, width=450, relief=SOLID, bg='white', bd=1)
canvas.pack()

points = 0
score = canvas.create_text(10,20, anchor=W, font='Arial 14', fill='brown', tex=points)

# Функции

def new_ball():
    red=randint(1,255)
    green=randint(1,255)
    blue=randint(1,255)

    global ball

    side = 50
    x = randint(0, 400)
    y = randint(0, 400)
    ball = canvas.create_oval(x,y,x+side,y+side, fill=f'#{red:02x}{green:02x}{blue:02x}',
    outline=f'#{red:02x}{green:02x}{blue:02x}')
    after_id = root.after(1000, lose)

    def click(event):
        if ball in canvas.find_overlapping(event.x, event.y, event.x, event.y):
            root.after_cancel(after_id)
            global points
            points += 1
            canvas.itemconfig(score, text=points)        
            canvas.delete(ball)
            new_ball()
        else:
            points -= 1
            canvas.itemconfig(score, text=points)    
    canvas.bind('<Button-1>', click)
def lose():
    global points
    points -= 1
    canvas.itemconfig(score, text=points)
    canvas.delete(ball)
    new_ball()  
new_ball()
# Конец программы
root.mainloop()