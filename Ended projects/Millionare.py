from tkinter import * 
from random import *
from tkinter import messagebox
from time import *

# Настройки окна
root = Tk() 
root.geometry('900x700+300+200')
root.configure(bg="#3700c1")
root.title(' ')
root.resizable(False, False)

# Функции
questions = [  
['Как заканчивается присказка: "Мы и сами с..."?', 'с волосами', 'с усами', 'с часами', 'с долгами', 'с усами'],
['Какой наиболее распространенный элемент на Земле?', 'воздух', 'вода', 'углерод', 'кислород', 'кислород'],
['Какое животное быстрее всех бегает по суше?', 'гепард', 'лев', 'тигр', 'волк', 'гепард'],
['Какое из этих чисел является простым?', '20', '33', '42', '47', '47'],
['Кто автор книги "1984"?', 'Рэй Брэдбери', 'Джордж Оруэлл', 'Айзек Азимов', 'Александр Солженицын', 'Джордж Оруэлл'],
['Как называется самая большая планета в Солнечной системе?', 'Марс', 'Юпитер', 'Венера', 'Сатурн', 'Юпитер'],
['Какой из этих языков программирования был разработан компанией Google?', 'Ruby', 'Python', 'Java', 'Go', 'Go'],
['В каком году произошла Русская революция?', '1917', '1905', '1914', '1922', '1917'],
['Как называется самый длинный река в мире?', 'Нил', 'Амазонка', 'Янцзы', 'Миссисипи', 'Амазонка'],
['Какой газ является основным компонентом воздуха?', 'кислород', 'углекислый газ', 'азот', 'водород', 'азот'],
['Кто написал роман "Мастер и Маргарита"?', 'Лев Толстой', 'Федор Достоевский', 'Михаил Булгаков', 'Андрей Платонов', 'Михаил Булгаков'],
['Как называется столица Японии?', 'Ханой', 'Пекин', 'Токио', 'Сеул', 'Токио'],
['Какой город является столицей Италии?', 'Милан','Флоренция', 'Венеция', 'Рим', 'Рим'],
['Какой национальности был физик Альберт Эйнштейн?', 'американской', 'швейцарской', 'немецкой', 'австрийской', 'немецкой'],
['Как называется сильнейший ветер на Земле?', 'ураган', 'циклон', 'торнадо', 'смерч', 'ураган']
]
numQue = 0
btns = questions[numQue][1:5]
shuffle(btns)
pic = PhotoImage(file='C:/Users/User/Desktop/Projects/pictures/logo.gif')

def check(otv):
    global numQue 
    if numQue == 14: 
        messagebox.showinfo("Congratulations!", "Вы прошли нашу игру до конца и победили!")
    if otv == questions[numQue][5]:
        result.config(text="Правильный ответ!")
        numQue+=1
        btns = questions[numQue][1:5]
        shuffle(btns)
        root.after(2000, update_question, numQue, btns)
    else:
        result.config(text='Не не не, давай ещё раз.')



def update_question(numQue, btns):
    queL.config(text=questions[numQue][0])
    btn1.config(text=btns[0], command=lambda: check(btns[0]))
    btn2.config(text=btns[1], command=lambda: check(btns[1]))
    btn3.config(text=btns[2], command=lambda: check(btns[2]))
    btn4.config(text=btns[3], command=lambda: check(btns[3]))
    result.config(text='')






# Виджеты


picL = Label(root, image=pic)
picL.pack(side=TOP)

queL = Label(root, text=questions[numQue][0], font='Verdana 22', background='#3700c1', fg='yellow')

btn1 = Button(root, text=btns[0], font="Verdana 22", width=20, command=lambda: check(btns[0]), background='#3700c1', fg='yellow')
btn2 = Button(root, text=btns[1], font="Verdana 22", width=20, command=lambda: check(btns[1]), background='#3700c1', fg='yellow')
btn3 = Button(root, text=btns[2], font="Verdana 22", width=20, command=lambda: check(btns[2]), background='#3700c1', fg='yellow')
btn4 = Button(root, text=btns[3], font="Verdana 22", width=20, command=lambda: check(btns[3]), background='#3700c1', fg='yellow')
result = Label(root, text="", font="Verdana 22", width=50, background='#3700c1', fg='yellow')


picL.grid(row=0, column=0, columnspan=3)
queL.grid(row=1, column=0, columnspan=2)
btn1.grid(row=2, column=0, padx=40)
btn2.grid(row=2, column=1, padx=40, pady=10)
btn3.grid(row=3, column=0)
btn4.grid(row=3, column=1)
result.grid(row=4, column=0, columnspan=3)



# Конец программы
root.mainloop()