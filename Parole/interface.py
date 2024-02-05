from tkinter import * 
from random import *
from main import *

# Настройки окна
root = Tk() 
root.geometry('380x380')
root.title(' ')
root.resizable(False, False)

# Функции
lowercase = BooleanVar()
uppercase = BooleanVar()
cip = BooleanVar()
cha = BooleanVar()

# Виджеты

symbols = LabelFrame(text="Символы", width=320, height=360)

s_char = Checkbutton(symbols, variable=lowercase, onvalue=True, offvalue=False , text="abcdefghijklmnopqrstuvwxyz")
spin_low = Spinbox(symbols, width=3, from_=1, to_=8, state='readonly', wrap=True)

l_char = Checkbutton(symbols,variable=uppercase, onvalue=True, offvalue=False , text='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
spin_up = Spinbox(symbols, width=3, from_=1, to_=8, state='readonly', wrap=True)

ciphers = Checkbutton(symbols, variable=cip, onvalue=True, offvalue=False , text='0123456789')
spin_cip = Spinbox(symbols, width=3, from_=1, to_=8, state='readonly', wrap=True)

char = Checkbutton(symbols, variable=cha, onvalue=True, offvalue=False ,  text='!@#$%^&*()')
spin_char = Spinbox(symbols, width=3, from_=1, to_=8, state='readonly', wrap=True)

password = Listbox(symbols, width=50, height=5)

button = Button(symbols, text="Сгенерировать пароль", width=20, command=pas)


symbols.pack(side=TOP, padx=15)
s_char.place(x=30, y=20)
spin_low.place(x=260,y=20)
l_char.place(x=30, y=60)
spin_up.place(x=260,y=60)
ciphers.place(x=30, y=100)
spin_cip.place(x=260,y=100)
char.place(x=30, y=140)
spin_char.place(x=260,y=140)
password.place(x=5, y=190)
button.place(x=65, y=300)
# Конец программы
root.mainloop()