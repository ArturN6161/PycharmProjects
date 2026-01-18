# def sum_uneven(n):
#     if n < 1:
#         return 0
#     if n % 2 != 0:
#         return n + sum_uneven(n - 2)
#     return sum_uneven(n - 1)


# print(sum_uneven(5))


# def factorial_3_5(n):
#     if n % 3 == 0 and n % 5 == 0 and n % 2 != 0:
#         return n * factorial_3_5(n - 2)
#     if n < 2:
#         return 1
#     return factorial_3_5(n - 1)


# print(factorial_3_5(45))



# Алгоритм вычисления значения функции F(n), где n – целое неотрицательное
# число, задан следующими соотношениями:
#
# F(0) = 0; # F(n) = F(n – 1) + 1, если n нечётно;
#
# F(n) = F(n/2), если n > 0 и при этом n чётно.
#
# Укажите количество таких значений n < 1 000 000 000, для которых F(n) = 2.

# def F(n):
#     if n == 0:
#         return 0
#     if n % 2 != 0:
#         return F(n - 1) + 1
#     if n % 2 == 0:
#         return F(n/2)


# counter = 0
# for i in range(1_000):
#     if F(i) == 2:
#         counter += 1

# print(counter)


# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:

# F(n) = 1 при n = 1;

# F(n) = 3 × n + F(n — 2), если n > 1 и при этом n нечётно,

# F(n) = 4 × F(n / 2), если n > 1 и при этом n чётно.

# Чему равно значение функции F(42)?


# def F(n):
#     if n == 1:
#         return 1
#     if n > 1 and n % 2 != 0:
#         return 3 * n + F(n - 2)
#     if n > 1 and n % 2 == 0:
#         return 4 * F(n / 2)


# print(F(42))


# Обозначим частное от деления целочисленного натурального числа a на натуральное число b как a div b, а остаток как a mod b. Например, 13 div 3 = 4, 13 mod 3 = 1.

# Алгоритм вычисления значения функции F(a, b), где a и b – целые неотрицательные числа, задан следующими соотношениями:

# F(0, b) = b;

# F(a, b) = F(a div 10, 10b + (a mod 10)), если a > 0.

# Укажите наименьшее значение a, для которого F(a, 0) = 1392781243.


# def F(a, b):
#     if a == 0:
#         return b
#     if a > 0:
#         return F(a // 10, 10 * b + (a % 10))

# a = 0
# while F(a, 0) != 1392781243:
#     a += 1
# print(a)

import time


def W(row, pos):
    if row < 1:  # точка остановки
        return 0
    if pos == row or pos == 0:  # край пирамиды
        return (1 + W(row - 1, pos)) / 2
    
    return (W(row - 1, pos - 1) + W(row - 1, pos)) / 2 + 1


print(W(20, 10))



