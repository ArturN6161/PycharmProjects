# Словарь (dict) - тип данных позволяющий хранить сложноструктурируемые данные
#from pprint import pprint
#import pprint for pprint
# coof = [1, 3, 2, 55, 3]
# users = {
#     'name': 'John',
#     'age': 55,
#     'citys': ['New-York', 'San Francisco', 'Washington'],
#     'address': {
#         'city': 'San Francisco',
#         'country': 'USA',
#         'postal_code': '10847'
#     }
# }

# pprint(users)
# print(users['citys'])
# print(users['address']['country'])

# citys = users.get('citys')
# if citys:
#     print(citys)
# else:
#     print('Человек не путешествует!')

# for k, v in users.items():
#     print(k, v)

# for i in users:
# kworg1 = {
#     'а': '7', 'б': '#', 'в': '2', 'г': '&', 'д': '9',
#     'е': '!', 'ё': '(', 'ж': '0', 'з': '@', 'и': '5',
#     'й': '$', 'к': '_', 'л': '1', 'м': ')', 'н': '6',
#     'о': '-', 'п': '4', 'р': '+', 'с': '=', 'т': '8',
#     'у': '[', 'ф': ']', 'х': '{', 'ц': '}', 'ч': '|',
#     'ш': ';', 'щ': ':', 'ъ': ',', 'ы': '.', 'ь': '<',
#     'э': '>', 'ю': '?', 'я': '/', ' ':' '
# }
#
# text = input("Введите текст для его шифрования: ")
# text1 = ""
#
# for i in text.lower():
#     text1 += kworg1.get(i)
#
# print(text1)
#
# kworg2 = {}
#
# for key, value in kworg1.items():
#     kworg2[value] = key
#
# text2 = ""
# for i in text1:
#     text2 += kworg2.get(i)
#
# print(text2)
#     print(i, users[i])

 #  print(*kworg2.values())

 #  print(f"key: {key}, value: {value}")

# list_dict = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
# kworg = {}
# print(list_dict)
# n = int(input("Введите единицу смещения для метода шифрования Цезаря: "))
#
# text = input("Введите текст который хотите зашифровать: ")
# text1 = ""
# for i in range(len(list_dict)):
#     new_index = (i + n) % len(list_dict)
#     kworg[list_dict[i]] = list_dict[new_index]
# for t in text.lower():
#     if t in kworg:
#         text1 += kworg.get(t)
#     else:
#         text1 += t
# print(f"Зашифрованный текст: {text1}")
# print(f"Исходный текст: {text}")

# numbers = range(1, 30)
# num2 = []
# for i in numbers:
#     i = i ** 2
#     num2.append(i)
# print(num2)

# colors = input("Введите последовательность цветов, разделенных дефисами: ")
# colors = colors.split("-")
# colors.sort()
#  #  белый-чёрный-жёлтый-зелёный-красный-фиолетовый-синий
# print(colors)
#
# colors = "-".join(colors)
# print(type(colors), colors)


# vowels = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
# consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
# digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
# special_characters = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', ';', ':', "'", '"', '\\', '|', ',', '.', '<', '>', '/', '?', '`', '~', ' ')
#
# v = 0
# c = 0
# d = 0
# s = 0
#
# text = input("Введите текст включающий буквы, цифры и спец. символы, чтобы посчитать их количества: ")
#
# for i in text:
#     if i.isalpha():
#         if i in vowels:
#             v += 1
#         else:
#             c += 1
#     if i.isdigit():
#         d += 1
#     if i in special_characters:
#         s += 1
#
#
# print(f"Количество гласных {v}, количество согласных {c}, количество цифр {d}, количество спец. символов {s}")

# lowers = 0
# uppers = 0
#
# text = input("Введите текст включающий заглавные буквы и строчные, чтобы посчитать их количества: ")
#
# for i in text:
#     if i.isalpha():
#         if i.isupper():
#             uppers += 1
#         elif i.islower():
#             lowers += 1
#
# print(f"Количество заглавных {uppers}, количество строчных {lowers}")

# n = int(input("Введите число печатающую квадраты всех натуральных чисел от 0 до заданного натурального n: "))
# list = []
# for i in range(n + 1):
#     i = i**2
#     list.append(i)
# print(list)

# n = int(input("Введите число печатающую факториал для заданного натурального n: "))
# list = [1]
# for i in range(1, n + 1):
#     i *= list[i-1]
#     list.append(i)
# print(list)

# n = int(input("Введите число вычисления последовательности Фибоначчи для заданного натурального n: "))
# list = []
# a, b = 0, 1
# for i in range(n + 1):
#     a, b = b, a + b
#     list.append(a)
# print(list)

# cats = 2
# days = 0
# miska = 100
# while cats <= miska:
#     days += 1
#     if days % 7 == 0:
#         cats += cats // 2
# print(f"Через {days} дней")
# print(f"Кошек: {cats}, останется голодных: {cats - miska}")

# page = 0
# sum_pages = 0
# page_input = 32
# sum_pages_input = 1201
#
# while page <= page_input:
#     sum_pages += page
#     page += 1
#
# print(f"Сумма страница на {page_input} равна {sum_pages} ")

# m = 100000
# s = 1000000
# p = 20
#
# days = 0
# current = m
# daily_p = p / 100 / 365
#
# while current < s:
#     current += current * daily_p
#     days += 1
#
# print(f"Через {days} дней долг составит {current:.2f} ₽")

# harvest = int(input("Урожай текущий: "))
# rate = 5
# years = 0
#
# double_harvest = harvest * 2
#
# while harvest < double_harvest:
#     harvest += harvest * rate / 100
#     years += 1
#
# print(f"Через {years} лет урожай удвоится")

# n = 0
# while n < 5:
#     n += 1
#     print(f"{n}. 000000")

# sum = 0
# for i in range(1,100):
#     sum += i
# print(sum)

# numbers = [i**2 for i in range(1, 20 + 1) if i % 3 == 0]
# print(numbers)

# words = ['apple', 'banana', 'orange', 'umbrella', 'grape', 'elephant']
# vowel = ['a', 'o', 'u', 'e']
# alpha = [word[:1] for word in words if word[:1] in vowel]
# # for word in words:
# #     if word[:1] in vowel:
# print(alpha)

# for i in range(20):
#     print("< > < > < > < > < >")
#     print(" ^   ^   ^   ^   ^ ")
#     print(" |   |   |   |   | ")

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for i in range(len(alphabet)//3):
#     print("^ " * 26)
#     print(f"|     {alphabet[i].upper()}   {alphabet[i].lower()}   | |     {alphabet[i+11].upper()}   {alphabet[i+11].lower()}     | |     {alphabet[i+22].upper()}   {alphabet[i+22].lower()}     |")
#     print("^ " * 26)

# import time
#
# #start = time.perf_counter()
#
# initial_num = int(input("Введите начальную точку отсчета: "))
# final_num = int(input("Введите конечную точку отсчета: "))
#
# for i in range(initial_num,final_num + 1):
#     print(i)
#     #time.sleep(1)
#     if i != final_num:
#         time.sleep(1)
# #end = time.perf_counter()
# #print(f"{end - start:.6f}")

from random import randint


difficulty_level = int(input("Введите номер уровеня сложности, где 1 - 'новичёк', 2 - 'спортсмен', 3 - 'мастер', 4 - 'зверь': " ))

newbie = 10
sportsmen = 25
master = 50
boss = 100


if difficulty_level == 1:
    level = newbie
elif difficulty_level == 2:
    level = sportsmen
elif difficulty_level == 3:
    level = master
elif difficulty_level == 4:
    level = boss

effort = 0
random_number = randint(1, level)
print(f"Попробуй отгадать число от 1 до {level}")

while True:
    number = int(input("Попробуй отгадать загаданное число: "))
    effort += 1
    if number == random_number:
        if effort <= 3:
            print("Удача на твоей стороне!")
        else:
            print(f"Поздравляем! Ты угадал!")
        print(f"Количество попыток: {effort}")
        break
    if number < random_number:
        print("Загаданное число БОЛЬШЕ")
    else:
        print("Загаданное число МЕНЬШЕ")