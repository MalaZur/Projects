import interface
from ciphers import caesar_encrypt 
from ciphers import atbach_encrypt
from ciphers import ceasar_affine_encrypt
def encrypt():
    if currentcipher == 'Цезарь':
        plaintext = interface.plaintextbox.get()
        key = int(interface.keybox1.get())
        textt = caesar_encrypt(plaintext, key)
        interface.ciphermessage.config(text=textt)
    elif currentcipher == 'Атбаш':
        plaintext = interface.plaintextbox.get()
        textt = atbach_encrypt(plaintext)
        interface.ciphermessage.config(text=textt)
    elif currentcipher == 'Афина':
        plaintext = interface.plaintextbox.get()
        key1 = int(interface.keybox1.get())
        key2 = int(interface.keybox2.get())
        textt = ceasar_affine_encrypt(plaintext, key1, key2)
        interface.ciphermessage.config(text=textt)

def change_cipher():
    global currentcipher
    currentcipher = interface.cho.get()
    if currentcipher == 'Цезарь':
        interface.ciphername.config(text='Зашифрованно шифром Цезаря')
        interface.keybox1.config(state='normal')
        interface.keybox2.config(state='disabled')
    elif currentcipher == 'Атбаш':
        interface.ciphername.config(text='Зашифрованно шифром Атбаш')
        interface.keybox1.config(state='disabled')
        interface.keybox2.config(state='disabled')
    elif currentcipher == 'Афина':
        interface.ciphername.config(text='Зашифрованно Аффинным шифром')
        interface.keybox1.config(state='normal')
        interface.keybox2.config(state='normal')


