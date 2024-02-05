from tkinter import * # Викторина
from random import *
from tkinter import messagebox

# Настройки окна
root = Tk() 
root.geometry('300x300')
root.title('Викторина')
root.resizable(False, False)

# Функции

def que_one():
    question = Label(root, text='Висит груша, нельзя скушать')
    answer = Entry()
    btn = Button(root, text='Ответить!', command=lambda: game1(que_two))
    question.pack(side=TOP)
    answer.pack(side=TOP)
    btn.pack(side=TOP)
    
    def game1(que_two):
        if answer.get().lower() == 'лампочка':
            que_two()
        else:
            messagebox.showerror('Неверно!', 'Вы ввели неправильный ответ')





def que_two():
    question_2 = Label(root, text='Зимой и летом одним цветом')
    answer_2 = Entry()
    btn_2 = Button( text='Ответить!', command=lambda: game2(que_two))
    question_2.pack(side=TOP)
    answer_2.pack(side=TOP)
    btn_2.pack(side=TOP)

    def game2(que_two):
        if answer_2.get().lower() == 'ёлка':
            messagebox.showinfo('Победа!', 'ПОБЕДА ЗА ОРДОЙ!')
        else:
            messagebox.showerror('Неверно!', 'Вы ввели неправильный ответ и Альянс победил')

que_one()

# Виджеты


# Конец программы
root.mainloop()