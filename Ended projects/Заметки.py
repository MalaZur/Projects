from tkinter import * # Заметки
from random import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

# Настройки окна
root = Tk() 
root.geometry('400x400')
root.title('Заметки')
root.resizable(False, False)

# Функции

def new_file():
    global file_name
    file_name = 'Без названия'
    text.delete('1.0', END)

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get(1.0, END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror('Ой!', 'Нельзя сохранить файл!')

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label='Новый', command = new_file)
file_menu.add_command(label='Открыть', command = open_file)
file_menu.add_command(label='Сохранить', command = save_as)


menu_bar.add_cascade(label='Файл', menu=file_menu)


root.config(menu=menu_bar)
# Виджеты

text = Text(root, width=400, height=400)
text.pack()

# Конец программы
root.mainloop()