# def palindrome(filename, mode):
#     with open(filename, mode) as file:
#         text = file.read().split()
#         counter = 0
#         for i in text:
#             if i == i[::-1]:
#                 print(i, '- Палиндром')
#                 counter += 1
#     return counter


# a = 'data.txt'
# m = 'r'
# # name = input()
# cou = palindrome(a, m)
# print('Количество палиндромов:', cou)


# def sum_number():
#     number_start = int(input('Введите стартовое число: '))
#     number_end = int(input('Введите последнее число: '))

#     i_start = number_start
#     i_end = number_end

#     if number_start > number_end:
#         i_start, i_end = number_end, number_start

#     sum_number = 0

#     for i in range(i_start, i_end + 1):
#         sum_number += 1
#     return sum_number, number_start, number_end

# summa, start_n, end_n = sum_number()

# print(f'Сумма диапазана:{start_n}, {end_n} -, равна: {summa}')

from datetime import datetime


def number_of_days(day_start, day_end):
    delta = day_end - day_start
    return delta.days


number_start = input('Введите первую дату (ГГГГ,ММ,ДД): ')
number_end = input('Введите вторую дату (ГГГГ,ММ,ДД): ')

day_start = datetime.strptime(number_start, '%Y,%m,%d')
day_end = datetime.strptime(number_end, '%Y,%m,%d')

delta_d = number_of_days(day_start, day_end)

print(f"Разница в днях: {delta_d}")