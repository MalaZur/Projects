from tkinter import * # Reaction
from random import *
import time

# Настройки окна
root = Tk() 
root.geometry('450x450')
root.title('Reaction')
root.resizable(False, False)
canvas = Canvas(height=450, width=450, relief=SOLID, bd=1, bg='white', )
canvas.pack(expand=True)

y = 20
count_of_clicks = 0

# Функции
def main():    
    global ball    
    ball = canvas.create_oval(175,275,275,175, fill='black')
    ran = randint(3000,7000)
    root.after(ran, start)
def start():
    global start_time
    start_time = time.time()
    canvas.itemconfig(ball, fill='green', outline='green')
    canvas.tag_bind(ball, '<Button-1>', click)
def click(event):
    global count_of_clicks
    global y
    click_time = time.time()
    seconds = round(click_time - start_time, 3)
    score = canvas.create_text(40,y, font='Arial 14', text=seconds)
    canvas.delete(ball)
    count_of_clicks += 1
    global results
    if count_of_clicks < 5:
        results = []
        results.append(seconds)
        y += 20
        root.after(500, main)
    else:
        canvas.create_text(225,225, anchor=CENTER, font='Arial 24', text=f'Ваше время реакции: {sum(results)/len(results)}')
        root.after(5000, restart)


def restart():
    global y
    global results
    global count_of_clicks
    y = 0
    results = []
    count_of_clicks = 0
    canvas.delete('all')
    main()

main()
# Конец программы
root.mainloop()