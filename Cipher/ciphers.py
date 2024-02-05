alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabetr = 'яюэьыъщшчцхфутсрпонмлкйизжёедгвба'
def caesar_encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext.lower(): # Решение проблемы-1
        # <Шифрование предложений>
        if letter.isspace():
            ciphertext += ' '
            continue
        # </Шифрование предложений>
        index = alphabet.find(letter)
        new_index = (index + key) % len(alphabet) # Решение проблемы-2
        new_letter = alphabet[new_index]
        ciphertext += new_letter
    return ciphertext

def atbach_encrypt(plaintext):
    ciphertext = ''
    for letter in plaintext.lower(): # Решение проблемы-1
        # <Шифрование предложений>
        if letter.isspace():
            ciphertext += ' '
            continue
        # </Шифрование предложений>
        index = alphabet.find(letter)
        new_index = (index) %len(alphabet) # Решение проблемы-2
        new_letter = alphabetr[new_index]
        ciphertext += new_letter
    return ciphertext

def ceasar_affine_encrypt(plaintext, key1, key2):
    divisors = calculate_divisors(alphabet)
    for i in range(len(divisors)):
        if key2 % divisors[i] == 0: return "Ключ не подходит"
    ciphertext = ''
    for letter in plaintext.lower(): # Решение проблемы-1
        # <Шифрование предложений>
        if letter.isspace():
            ciphertext += ' '
            continue
        # </Шифрование предложений>
        index = alphabet.find(letter)
        new_index = (index * key2 + key1) % len(alphabet) # Решение проблемы-2
        new_letter = alphabet[new_index]
        ciphertext += new_letter
    return ciphertext



def calculate_divisors(n):
    o = []
    for i in range(2, len(n)+1):
        if len(n) % i == 0:
            o.append(i)
    return o