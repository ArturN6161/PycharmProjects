# products = {}

# try:
#     while True:
#         print()
#         vote = input("Хотите добавить в ассортимент товаров продукт? ")
#         if vote in ['y','yes','д','да', '']:
#             while True:
#                 try:
#                     name = input('Введите наименование товара: ').strip().lower()
#                     if name not in products:
#                         price = int(input('Введите цену товара: '))
#                         if 0 < price: 
#                             products[name] = price
#                             print(f'Товар успешно добавлен {name}, {price}.')
#                             print(f'Оставшиеся товары {products}.')
#                             break
#                         else:
#                             print(f'Для товара {name} установлена некорректная цена {price}. Введите положительное число.')
#                     else:
#                         print(f'Товар уже с названием {name} уже есть в ассортименте.')
#                 except ValueError:
#                     print('Введите положительное число.')
#         else:
#             break   

#     while True:
#         print(products)
#         vote = input("Хотите удалить из ассортимента товаров продукт? ")
#         if vote in ['y','yes','д','да', '']:
#             while True:
#                 name = input('Введите наименование товара: ').strip().lower()
#                 if name in products:
#                     products.pop(name)
#                     print(f'Товар {name} был удалён.')
#                     print(f'Оставшиеся товары {products}.')
#                     break
#                 else:
#                     print(f'Товар {name} не найден.')
#         else:
#             print(f'Оставшиеся товары {products}')
#             break

#     total = 0
#     for i in products:
#         total += products.get(i)
#     print(f'Общая сумма товаров: {total}.')
# except KeyboardInterrupt:
#     print('Программа была прервана пользователем.')

# from datetime import datetime, timedelta

# start_time = int(input('Enter number 1: '))
# end_time = int(input('Enter number 2: '))


# def delta_time(start_time, end_time):
#     start_time = timedelta(seconds=start_time)
#     end_time = timedelta(seconds=end_time)
#     delta_sec = abs(end_time - start_time)
#     days = delta_sec.days
#     hours = delta_sec.seconds // 3600
#     minutes = (delta_sec.seconds % 3600) // 60
#     seconds = delta_sec.seconds % 60
#     return days, hours, minutes, seconds


# days, hours, minutes, seconds = delta_time(start_time, end_time)

# print(f"Разница между {start_time} сек. и {end_time} сек.:")
# print(f"{days} дней, {hours} часов, {minutes} минут, {seconds} секунд.")