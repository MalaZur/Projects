import interface
from tkinter import *
from generator import generate_password

def pas():
    interface.password.delete(0, END)
    for i in range(5):
        password_str = generate_password(interface.lowercase.get(), interface.uppercase.get(), interface.cip.get(), interface.cha.get(), int(interface.spin_low.get()), int(interface.spin_up.get()), int(interface.spin_cip.get()), int(interface.spin_char.get()))
        interface.password.configure(justify='center')
        interface.password.insert(END, password_str)