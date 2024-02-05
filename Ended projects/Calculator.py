from tkinter import * # калькулятор
from random import *
from tkinter import messagebox
from tkinter import ttk



# Настройки окна
root = Tk() 
root.title('Калькулятор')
root.resizable(False, False)


def calc(key):
    global memory
    if key == '=':
#Без букв
        str1 = '+-0123456789.*/'
        if calc_entry.get() [0] not in str1:
            calc_entry.delete(0,END)
            calc_entry.insert(END, 'Неверный первый символ!')
            messagebox.showerror('Ошибка!', 'Вы ввели не число!')
#счёт
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
        except:
            calc_entry.delete(0,END)
            calc_entry.insert(END, 'Ошибка!')
            messagebox.showerror('Ошибка!', 'Проверь правильность данных!')
#очистка
    elif key == 'C':
        calc_entry.delete(0, END)
#счёт +/-
    elif key == '-/+':
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get() [0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

button_list = [
    '7', '8', '9', '+', '-',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '-/+', '=',
    '0', '.', 'C', 
]

r = 1
c = 0

# Функции

for i in button_list:
    rel = ''
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i,command=cmd).grid(row=r, column=c)
    c += 1
    if c>4:
        c=0
        r += 1


# Виджеты

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)
# Конец программы
root.mainloop()