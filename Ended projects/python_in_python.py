from tkinter import * 
from random import *

# Настройки окна
root = Tk() 
root.geometry('1000x750')
root.title(' ')
root.resizable(False, False)

WIDTH = 1000
HEIGHT = 750

SEG_SIZE = 20
IN_GAME = True

c = Canvas(width=WIDTH, height=HEIGHT, bg='#003300')
c.grid()
c.focus_set()

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x,y, x+SEG_SIZE, y+SEG_SIZE, fill="white")

class Snake(object):
    def __init__(self, segments):
        self.segments = segments
        self.mapping = {"Down":(0,1), "Up":(0,-1), "Left":(-1,0), "Right":(1,0)}
        self.vector = self.mapping["Right"]
    def move(self):
        for i in range(len(self.segments)-1):
            segment = self.segments[i].instance
            x1,y1,x2,y2 = c.coords(self.segments[i+1].instance)
            c.coords(segment,x1,y1,x2,y2)
        x1,y1,x2,y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance, 
                x1 + self.vector[0]*SEG_SIZE,
                y1 + self.vector[1]*SEG_SIZE,
                x2 + self.vector[0]*SEG_SIZE,
                y2 + self.vector[1]*SEG_SIZE)
    def change_direction(self, event):
        if event.keysym in self.mapping:
            new_direction = self.mapping[event.keysym]
            if (new_direction[0] == 1 and self.vector[0] == -1) or \
               (new_direction[0] == -1 and self.vector[0] == 1) or \
               (new_direction[1] == 1 and self.vector[1] == -1) or \
               (new_direction[1] == -1 and self.vector[1] == 1):
                return
            self.vector = new_direction
    def add_segment(self):
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x,y))

segments = [Segment(SEG_SIZE, SEG_SIZE), Segment(SEG_SIZE*2, SEG_SIZE), Segment(SEG_SIZE*3, SEG_SIZE)]
s = Snake(segments)

def create_block():
    global BLOCK
    posx = SEG_SIZE * (randint(1, (WIDTH - SEG_SIZE) // SEG_SIZE))
    posy = SEG_SIZE * (randint(1, (HEIGHT - SEG_SIZE) // SEG_SIZE))
    block_coords = (posx, posy, posx + SEG_SIZE, posy + SEG_SIZE)
    
    overlap = False
    for segment in s.segments:
        if c.coords(segment.instance) == block_coords:
            overlap = True
            break
    if not overlap:
        BLOCK = c.create_oval(posx, posy, posx + SEG_SIZE, posy + SEG_SIZE, fill="red")

c.bind("<KeyPress>", s.change_direction)
create_block()

def main():
    global IN_GAME
    global BLOCK
    if IN_GAME:
        s.move()
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        if x1 < 0 or x2 > WIDTH or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()
        else:
            for i in range(len(s.segments) - 1):
                if c.coords(s.segments[i].instance) == head_coords:
                    IN_GAME = False
        root.after(100, main)
    else:
        c.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", font="Arial 20", fill="#ff0000")


main()

    


# Конец программы
root.mainloop()