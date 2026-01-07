from math import pi
try:
    r = int(input('Введите радиус окружности: '))
    S = pi * r**2
    P = 2 * pi * r
    print(f'Окружность с радиусом {r} имеет площадь: {S:.2f} и периметр: {P:.2f}')
except ValueError:
    print("Некорректный тип данных. Введите целое натуральное число!")

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(f'Окружность с радиусом {r} имеет площадь: {S:.2f} и периметр: {P:.2f}')