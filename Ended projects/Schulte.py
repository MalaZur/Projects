import time
from tkinter import * # Шульте чёртов
from random import *
from tkinter import messagebox

# Настройки окна
root = Tk() 
root.geometry('550x300')
root.title('Schulte')
root.resizable(False, False)

# Функции

def restart():
    ready = messagebox.askyesno('Готовы?','После нажатия "Да" будет отсчитываться время...')
    if ready == True:
        start_time = time.time()
        label.forget()
        button.forget()
        numbers_in_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        random_numbers = [i for i in range (1,10)]
        shuffle(random_numbers)
        game_frame = Frame()
        game_frame.pack()
        r = 0
        c = 0
        num_button = Button(game_frame, font=('Arial', 15, 'bold'), width=8, height=3, text=random_numbers[0])
        num_button.grid(row=0, column=0)
        for i in range(1,len(numbers_in_order)):
            num_button = Button(game_frame, font=('Arial', 15, 'bold'), width=8, height=3, text=random_numbers[i])
            c += 1
            if c == 3:
                r += 1
                c = 0
            num_button.grid(row=r, column=c)
            def click(event):    
                if str(numbers_in_order[0]) > str(event.widget['text']):
                    event.widget.config(state=DISABLED)
                elif event.widget['text'] == 'Начать игру': #Это нужно что бы после нажатия esc не вылетала ошибка что нажата не та кнопка
                    restart()
                elif str(numbers_in_order[0]) == str(event.widget['text']):
                    event.widget['bg'] = 'green'
                    del numbers_in_order[0]
                    event.widget.unbind('<Button-1>') # Эта мразь не работает, по этому мне пришлось сделать нерабочий 'Костыль' что бы у меня не вылетала ошибка
                    event.widget.config(state=DISABLED)
                elif str(numbers_in_order[0]) != str(event.widget['text']):
                    messagebox.showerror('Уупс!','Вы ошиблись!\nНачинайте сначала')
                    game_frame.destroy()
                    restart()
                if len(numbers_in_order) == 0:
                    end_time = time.time()
                    user_time = end_time - start_time
                    messagebox.showinfo('Поздравляем!',f'Вы победили\nВаше время:{round(user_time, 3)}')
                    game_frame.destroy()
                    label.pack(expand=True)
                    button.pack(expand=True)
            def main_menu(event):
                answer = messagebox.askyesno('Вопрос','Вы уверены, что хотите прервать игру?')
                if answer == True:
                    game_frame.destroy()
                    label.pack(expand=True)
                    button.pack(expand=True)
            root.bind('<Button-1>', click)
            root.bind('<Escape>', main_menu)

    

        
# Виджеты

label = Label( text='Шульте - это простая игра, которая развивает\nпереферическое зрение, скорость чтения и\nреакцию!\nПравила игры:\n1. Игрок должен быстрее всех выбрать все числа по порядку от 1 до 9.\n2. Если игрок ошибается - игра начинается заново.\n3. Побеждает тот, кто быстрее всех справится с\nзадачей.', font=('Arial', 10), justify=LEFT)
label.pack(side=TOP, pady=40)
button = Button(text='Начать игру', command=restart)
button.pack(side=TOP)
# Конец программы
root.mainloop()