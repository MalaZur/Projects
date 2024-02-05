#numbers = list(map(lambda x: int(x) / 1.6, input("Введите через пробел километры: ").split()))
#print(numbers)
#
#
#words = ["first", "second", "third"]
#r_words = list(map(lambda x: x[::-1], words))
#print(r_words)
#
#phrase = 'abcdefg'
#ascii_list = list(map(lambda char: ord(char)-96, phrase))
#print(ascii_list)

strings = ['1', 'echo','2', '4', 'aboba']

#1-ый способ
def is_number(string):
    return string.isdigit()

number = list(filter(is_number, strings))
print(number)
#2-ой способ
number_2 = list(filter(lambda string: string.isdigit(), strings))
print(number)


numbers_aboba = [-1, 2, -3, 32, -43, 3, 5]
number_mt_0 = list(filter(lambda x: x>0, numbers_aboba))
print(number_mt_0)


list_1 = [1,2,3,5,8,13,21,34,55,89]
list_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

common_elements = list(filter(lambda x: x in list_2, list_1))
print(common_elements)




        