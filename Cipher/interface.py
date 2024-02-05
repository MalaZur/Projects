from tkinter import * 
from random import *
from main import *
# Настройки окна
root = Tk() 
root.geometry('320x390')
root.title('Шифрование')
root.resizable(False, False)

# Функции


# Виджеты
choice = LabelFrame(text="Выбор шрифта: ", width=280, height=150)
cho = StringVar()
radioceasar = Radiobutton(choice, text="Шифр Цезаря", variable=cho, value="Цезарь", command=change_cipher)
radioatbach = Radiobutton(choice, text="Шифр Атбаш", variable=cho, value="Атбаш", command=change_cipher)
radioaffine = Radiobutton(choice, text="Аффинный шифр Цезаря", variable=cho, value="Афина", command=change_cipher)

data = LabelFrame(text="Данные", width=280, height=100)
text = Label(data, text='Введите текст: ', pady=10,padx=10)
key1 = Label(data, text="Ключ 1: ")
key2 = Label(data, text="Ключ 2: ")
plaintextbox = Entry(data)
keybox1 = Entry(data, width=7)
keybox2 = Entry(data, width=7)

c_message = LabelFrame(text="Зашифрованные сообщения", width=280, height=100)
ciphername = Label(c_message, text="Шифр Цезаря: ")
ciphermessage = Label(c_message, text="")

btn = Button(text="Зашифровать", height=1, command=encrypt)

choice.pack(side=TOP)
radioceasar.pack(side=TOP, padx=87)
radioatbach.pack(side=TOP, pady=8)
radioaffine.pack(side=TOP)

data.pack(side=TOP)
text.place(x=15, y = 0)
plaintextbox.place(x=5, y = 40)
key1.place(x=150, y = 9)
key2.place(x=220, y=9)
keybox1.place(x=150, y = 40)
keybox2.place(x=220, y=40)

c_message.pack(side=TOP)
ciphername.pack(side=TOP, padx=45, pady=10)
ciphermessage.pack(side=TOP, pady=10)

btn.pack(side=TOP, pady=15)

cho.set("Афина")
change_cipher()

# Конец программы
root.mainloop()