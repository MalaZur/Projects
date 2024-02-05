from random import *

def generate_password(s_char, l_char, ciphers, char, spin_1, spin_2, spin_3, spin_4):
    s_charr = 'abcdefghijklmnopqrstuvwxyz'
    l_charr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphersr = '0123456789'
    charr = '!@#$%^&*()'
    password = []
    if s_char == True: 
        for i in range(spin_1):
            password.append(s_charr[randint(0,25)])
    if l_char == True:
        for i in range(spin_2):
            password.append(l_charr[randint(0,25)])
    if ciphers == True:
        for i in range(spin_3):
            password.append(ciphersr[randint(0,9)])
    if char == True:
        for i in range(spin_4):
            password.append(charr[randint(0,9)])
    shuffle(password)
    password_str = ''.join(password)
    return password_str
