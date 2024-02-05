from tkinter import * # Morze
from winsound import *
from time import *

# Настройки окна
root = Tk() 
root.geometry('500x300')
root.title('Morze')
root.resizable(False, False)

mc = {'A': ['.-', 'A.wav'],
'B': ['-...', 'B.wav'],
'C': ['-.-.', 'C.wav'],
'D': ['-..', 'D.wav'],
'E': ['.', 'E.wav'],
'F': ['..-.', 'F.wav'],
'G': ['--.', 'G.wav'],
'H': ['....', 'H.wav'],
'I': ['..', 'I.wav'],
'J': ['.---', 'J.wav'],
'K': ['-.-', 'K.wav'],
'L': ['.-..', 'L.wav'],
'M': ['--', 'M.wav'],
'N': ['-.', 'N.wav'],
'O': ['---', 'O.wav'],
'P': ['.--.', 'P.wav'],
'Q': ['--.-', 'Q.wav'],
'R': ['.-.', 'R.wav'],
'S': ['...', 'S.wav'],
'T': ['-', 'T.wav'],
'U': ['..-', 'U.wav'],
'V': ['...-', 'V.wav'],
'W': ['.--', 'W.wav'],
'X': ['-..-', 'X.wav'],
'Y': ['-.--', 'Y.wav'],
'Z': ['--..', 'Z.wav'],
'0': ['-----', '0.wav'],
'1': ['.----', '1.wav'],
'2': ['..---', '2.wav'],
'3': ['...--', '3.wav'],
'4': ['....-', '4.wav'],
'5': ['.....', '5.wav'],
'6': ['-....', '6.wav'],
'7': ['--...', '7.wav'],
'8': ['---..', '8.wav'],
'9': ['----.', '9.wav'],
' ': [' ', '']}



def code():
    lo1.delete(0, END)
    s = ''
    for l in en01.get().upper():
        s = mc[l][0] + ' '
        lo1.insert(END,s)
        if l != ' ':
            PlaySound('C:/Users/User/Desktop/Projects/morze/' + mc[l][1], SND_FILENAME)
        else: sleep(0.5)



lo1 = Entry(root, font='Verdana 28', justify=CENTER)
en01 = Entry(root, font='Verdana 28')
btn01 = Button(root, text='Send', font='Verdana 28', command=code)
lo1.insert(END, "Write text:")

lo1.pack(pady=5)
en01.pack()
btn01.pack()

root.mainloop()