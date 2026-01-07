# # # # # # x = int(input())
# # # # # # y = int(input())
# # # # # # if x > y:
# # # # # #     print(x)
# # # # # # else:
# # # # # #     print(y)
#
# # # # # health = int(input())
# # # # # water = int(input())
# # # # # if health + water == 0 and health + water < 0:
# # # # #     print("Ваш герой мёртв!")
# # # # # else:
# # # # #     print("Ваш герой жив!")
#
# # # # n = int(input())
# # # # if n % 2 == 0:
# # # #     print("True")
# # # # else:
# # # #     print("False")
#
# # # for i in range(1, 497):
# # #     if i % 2 == 0:
# # #         print(i, end = " ")
#
# # r = 0
# # for i in range(1, 100):
# #     r += i
# # print(r)
#
# # m = int(input())
# # if  m in (12, 1, 2):
# #     print("Зима")
# # elif m in (3, 4, 5):
# #     print("Весна")
# # elif m in (6, 7, 8):
# #     print("Лето")
# # else:
# #     print("Осень")
# # n = 1
# # while n < 5:
# #     print(n, "00000")
# #     n += 1
# #--------------------
# # N = int(input())
# # n0 = 0
# # while n0 < N + 1:
# #     print(n0)
# #     n0 += 1
# #
# # N = int(input())
# # K = int(input())
# #
# # if K > N:
# #     while N <= K:
# #         print(N)
# #         N += 1
#
# # N = int(input())
# # while N >= 0:
# #     print(N)
# #     N -= 1
# #
# # N = int(input())
# # while True:
# #     N = N // 3
# #     if N % 3 != 0:
# #         break
# # if N == 1:
# #     print("YES")
# # else:
# #     print("NO")
#
# # N = int(input("Введите положительное целое число: "))
# # n = 0
# # sum = 0
# # while n <= N:
# #     if n % 2 == 0:
# #         sum += n
# #     n += 1
# # print("Сумма всех чётных числен равна: ", sum)
#
# # sum = 0
# # print("Введите 2 положительных числа, где N > K")
# # N = int(input("Введите первое положительное целое число N: "))
# # K = int(input("Введите второе положительное целое число K: "))
# # while K <= N:
# #     if K % 2 != 0:
# #         sum += K
# #     K += 1
# # if N > K:
# #     print("Сумма всех нечётных числен равна: ", sum)
# # else:
# #     print("N должно быть больше K")
#
# # n = int(input("Введите число для рассчета факториала этого числа: "))
# # n1 = 1
# # product = 1
# #
# # while n1 <= n:
# #     product *= n1
# #     n1 += 1
# # print("Факториал числа", n, "равно: ", product)
#
# # number = input("Введите любое число для поиска наибольшей цифры в этом числе: ")
# # nmax = 0
# # for i in number:
# #     if int(i) > nmax:
# #         nmax = int(i)
# # print(nmax)
#
# # n = int(input("Введите любое число: "))
# # sum = 0
# # for i in range(1, n + 1):
# #     sum += i**(-1)
# # print(sum)
# #
# # n = int(input("Введите любое число: "))
# # sum = 0
# # for i in range(n + 1):
# #     sum += 2 ** i
# # print(sum)
#
# #
# # n = int(input("Введите любое число: "))
# # sum = 0
# # for i in range(1, n + 1):
# #     sum += 1 + 0.1 * i
# # print(sum)
#
#
# n = int(input("Введите любое число: "))
# sum = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum -= 1 + 0.1 * i
#     else:
#         sum += 1 + 0.1 * i
# print(sum)

# n = int(input("Введите любое число: "))
# sum = 0
# i = 1
# while n ** 2 > sum:
#     sum += i
#     print(sum)
#     i += 2
 #  ~~~~~~~~~~~~~~~~~~~
# list1 = list(range(1000))
# print(list1[371:782])
  #  ______________
# list1 = list(range(10000))
# X = int(input())
# if X in list1:
#     print(7145)
# else:
#     print(5741)

# a = {"asdasd", 1, "082379924", 5, 4, 9}
# print(a)

price = ["Карандаш", "Ручка", "Линейка", "Тетрадь", "Ластик", "Корректор"]

print(price)

action = input("Что хотите сделать? Ввведите одно из действий: найти, добавить, удалить или изменить: ")

if action.lower() == "найти":
    action = input("Введите наименование: ")
    if action in price:
        print(price[int(action)])
    else:
        print("Такого наименования нет")

if action.lower() == "добавить":
    action = price.append(input("Добавить в конец списка: "))
    print(price)

if action.lower() == "удалить":
    action = int(input("Какой индекс удалить? "))
    if action in price:
        price.pop(action)
        print(price)
    else:
        print("Такого индекса нет")

if action.lower() == "изменить":
    index = input("Какой индекс хотите изменить? ")
    if index.isdigit():
        if int(index) in range(len(price)):
            new_action = input("Введите новое значение: ")
            price.pop(int(index))
            price.insert(int(index), new_action)
            print(price)
        else:
            print("Такого индекса нет")
    else:
        print("Нужно ввести число, а не текст")




