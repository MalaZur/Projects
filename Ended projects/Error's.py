from tkinter import * #обработка ошибок
from random import *
from tkinter import messagebox

# Настройки окна
windows = Tk() 
windows.geometry('550x300')
windows.title('Решатель примеров')
windows.resizable(False, False)

# Функции

def equate():
    if equation.get() == "Богдан":
        messagebox.showinfo('Вы вызвали гнев древнего божества!', 'Ждите бана в течении следующих 5-ти секунд')
    try:
        solution = eval(equation.get())
    except SyntaxError:
        messagebox.showinfo('Внимание!', 'Вы что-то пропустили, пересмотрите пример')   
    except NameError:
        messagebox.showinfo('Ошибка!', 'Вы написали что-то совсем неправильное')
    except ZeroDivisionError:
        messagebox.showinfo('Серьёзно?!', 'Вы что, делите на ноль?')
    messagebox.showinfo('Готово!', f'Решение найдено: {solution}')
    
# Виджеты

frame = Frame()
frame.pack(side=TOP, pady=30)
label = Label(text='Введите математическое выражение из чисел и знаков \n+ - * / // % **')
label.pack(side=TOP, pady=20)
equation = Entry(width=50)
equation.pack(side=TOP, pady=20)
button = Button(text='Решить!', height=1, width=30, command=equate)
button.pack(side=TOP)
equation.focus()


# Конец программы
windows.mainloop()