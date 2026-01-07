from random import randint


#  Основной цикл игры
def play_game(random_number, level):
    effort = 0 #  Кол-во попыток
    try:
        while True:
            try:
                number = int(input("Попробуй отгадать загаданное число: "))
                effort += 1
                if number == random_number:
                    if effort <= 3:
                        print("Удача на твоей стороне!")
                    else:
                        print(f"Поздравляем! Ты отгадал!")
                    print(f"Количество попыток: {effort}")
                    break
                if number < 1 or number > level:
                    print("Загаданное число ВНЕ диапазона")
                elif number < random_number:
                    print("Загаданное число БОЛЬШЕ")
                else:
                    print("Загаданное число МЕНЬШЕ")

            except ValueError:
                print("Неверный ввод! Введите число")
    except KeyboardInterrupt:
        print(f"\nИгра была прервана пользователем. \nЗагаданное число было {random_number}")
        exit()


def choice_lvl():
    levels = {1: 10, 2: 25, 3: 50, 4: 100}
    try:
        difficulty_level = int(input("Введите номер уровня сложности, где 1 - 'новичёк', 2 - 'спортсмен', 3 - 'мастер', 4 - 'зверь': "))
        level = levels.get(difficulty_level, 10) #  Здесь определяем вехний диапазон загаданного числа
        if difficulty_level not in levels: #  Если уровень сложности введен не 1-4
            print("Неверный уровень! Установлен 'новичёк'")
    except ValueError: #  Если было введено не цифра сложности
        level = 10
        print("\nОшибка ввода! Установлен уровень 'новичёк'")
    except KeyboardInterrupt:
        print("\nИгра была прервана пользователем!")
        exit()
    random_number = randint(1, level)
    print(f"Загаданное число  от 1 до {level}")
    return random_number, level


#  Спрашиваем, хочет ли играть еще
def play_again():
    play_again = input("\nХочешь сыграть еще раз? (да/нет): ").lower()
    if play_again in ["no", "n", "нет", "н", "exit"]:
        print("Спасибо за игру!")
        return False


random_number, level = choice_lvl()

play_game(random_number, level)

while True:
    if play_again() is False:
        break
    else:
        random_number, level = choice_lvl()
        play_game(random_number, level)






