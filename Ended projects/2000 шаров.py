from tkinter import * # Рандомные 2000 шаров
from random import *

# Настройки окна
root = Tk() 
root.geometry('1920x1080')
root.title(' ')
root.resizable(True, True)

# Функции


# Виджеты
canvas = Canvas(width=1920, height=1080, relief=SOLID, bd=1, bg='white')
canvas.pack(side=TOP)
for i in range(5000):
    red=randint(0,255)
    green=randint(0,255)
    blue=randint(0,255)

    red2=randint(0,255)
    green2=randint(0,255)
    blue2=randint(0,255)

    x=randint(0,1920)
    y=randint(0,1000)
    side=randint(10,100)
    canvas.create_oval(x,y, x+side,y+side,fill=f'#{red:02x}{green:02x}{blue:02x}', outline='black', width=2)
    root.update()

# Конец программы
root.mainloop()