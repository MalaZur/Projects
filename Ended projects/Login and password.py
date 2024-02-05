from tkinter import * # Login and password
from random import *
from tkinter import messagebox
import pickle

# Настройки окна
root = Tk() 
root.geometry('300x400')
root.title('Войти в систему')
root.resizable(False, False)

# Функции

def registration():
    text = Label(text='Для входа в систему - зарегистрируйтесь!')
    text_log = Label(text='Введите Ваш логин:')
    registr_login = Entry()
    text_password_1 = Label(text='Введите Ваш пароль:')
    registr_password_1 = Entry()
    text_password_2 = Label(text='Введите Ваш пароль повторно:')
    registr_password_2 = Entry(show='*')
    button_registr = Button(text='Зарегистрироваться!', command=lambda: save())
    text.pack()
    text_log.pack()
    registr_login.pack()
    text_password_1.pack()
    registr_password_1.pack()
    text_password_2.pack()
    registr_password_2.pack()
    button_registr.pack()
    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()] = registr_password_1.get()
        f = open('login.txt', 'wb')
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text='Поздравляем! Теперь Вы можете войти в систему!')
    text_log.pack()
    text_enter_login = Label(text='Введите Ваш логин:')
    text_enter_login.pack()
    enter_login = Entry()
    enter_login.pack()
    text_enter_pass = Label(text='Введите Ваш пароль:')
    text_enter_pass.pack()
    enter_pass = Entry(show='*')
    enter_pass.pack()
    button_enter = Button(text='Войти', command=lambda: pass_check())
    button_enter.pack()
    
    def pass_check():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo('Вход в систему','Поздравляем! Вы успешно вошли в систему!')
            else:
                messagebox.showerror('Ошибка!', 'Вы ввели неверный логин или пароль!')
        else:
            messagebox.showerror('Ошибка!','Неверный логин!')


registration()
# Виджеты



# Конец программы
root.mainloop()