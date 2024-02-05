from tkinter import * # Вычисление корня из квадратного уравнения 
from random import *
from math import sqrt
from tkinter import messagebox

# Настройки окна
root = Tk() 
root.geometry('250x300')
root.title('Решатель уравнений')
root.resizable(False, False)

# Функции

def equate():
    output.delete(1.0,END)
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        answer = messagebox.askyesno('Проверка', f'Вы уверены что хотите решить уравнение со значениями {a}, {b} и {c}?')
        if answer == True:
            d = b**2 - 4*a*c
            if d >= 0:
                x1 = (-b + sqrt(d)) / (2*a)
                x2 = (-b - sqrt(d)) / (2*a)
                output.insert(END, f'Дискриминант равен {d}\nx1 = {x1}\nx2 = {x2}')
            else:
                output.insert(END, f'Дискриминант равен {d}\nУравнение не имеет решения')
        else:
            output.delete(1.0, END)
    except:
        output.insert(END, 'Убедитесь что все 3 числа \nвведены корректно')

def click(event):
    equate()
def help(event):#Вот это чёт не фокусируется, хотя с виджетом output всё работает, хмммм
    if event.widget == label_a:
        messagebox.showinfo('Информация', f'Введите число a')
    elif event.widget == label_b:
        messagebox.showinfo('Информация', f'Введите число b')
    elif event.widget == label_c:
        messagebox.showinfo('Информация', f'Введите число c')

def clear(event):
    a = event.widget
    try:
        a.delete(0,END)
    except:
        a.delete(1.0, END)

# Виджеты
root.bind('<Return>', click)
root.bind('<F1>', help)
root.bind('<Button-1>', clear)
root.bind('<Control-Key-1>', lambda event: entry_a.focus())
root.bind('<Control-Key-2>', lambda event: entry_b.focus())
root.bind('<Control-Key-3>', lambda event: entry_c.focus())


data = LabelFrame(text='Введите исходные данные')  #Вводные данные
entry_a = Entry(data, width=4)
entry_b = Entry(data,width=4)
entry_c = Entry(data,width=4)
label_a = Label(data, text='x**2')
label_b = Label(data, text='x+')
label_c = Label(data, text='=0')
data.pack(pady=20)
entry_a.pack(side=LEFT, padx=5, pady=5)
label_a.pack(side=LEFT, padx=5, pady=5)
entry_b.pack(side=LEFT, padx=5, pady=5)
label_b.pack(side=LEFT, padx=5, pady=5)
entry_c.pack(side=LEFT, padx=5, pady=5)
label_c.pack(side=LEFT, padx=5, pady=5)

result = LabelFrame(text='Решение')  
output = Text(result, width=28, height=5)
result.pack()
output.pack(padx=5, pady=10)

button = Button(text='Решить уравнение', command=equate)
button.pack(pady=20)

# Конец программы
root.mainloop()