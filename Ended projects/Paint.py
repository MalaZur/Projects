from tkinter import * # Paint
from random import *

# Настройки окна
root = Tk() 
root.geometry('700x600')
root.title('Paint on Python')
root.resizable(True, True)
brush_size = 3
color = 'black'

# Функции
def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1,y1,x2,y2,fill=color,outline=color)

def brush_size_change(new_size):
    global brush_size
    brush_size = new_size

def color_change(new_color):
    global color
    color = new_color

# Виджеты
col = Label(text='Цвета: ')
col.grid(row=0, column=1)
size = Label(text='Размер кисти: ')
size.grid(row=1, column=1)
red_btn = Button(text='Красный', width=10, height=2, command=lambda: color_change('red'))
red_btn.grid(row=0,column=2)
blue_btn = Button(text='Синий', width=10, height=2, command=lambda: color_change('blue'))
blue_btn.grid(row=0,column=3)
black_btn = Button(text='Черный', width=10, height=2, command=lambda: color_change('black'))
black_btn.grid(row=0,column=4)
white_btn = Button(text='Ластик', width=10, height=2, command=lambda: color_change('white'))
white_btn.grid(row=0,column=5)
clear_btn = Button(text='Удалить всё', width=10,command=lambda: w.delete('all'))
clear_btn.grid(row=0,column=6, sticky=W)

th_btn = Button(text='3', width=10, command=lambda: brush_size_change(3))
th_btn.grid(row=1,column=2)
f_btn = Button(text='5', width=10, command=lambda: brush_size_change(5))
f_btn.grid(row=1,column=3)
e_btn = Button(text='8', width=10, command=lambda: brush_size_change(8))
e_btn.grid(row=1,column=4)
ten_btn = Button(text='10', width=10, command=lambda: brush_size_change(10))
ten_btn.grid(row=1,column=5)
w = Canvas(root, width=700, height=500, bg='white')
w.bind('<B1-Motion>', paint)
w.grid(column=0,row=2,columnspan=7,pady=5,padx=5,sticky=E+W+S+N)
w.columnconfigure(6,weight=1)
w.rowconfigure(2,weight=1)

# Конец программы
root.mainloop()