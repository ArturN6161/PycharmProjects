def hello_screen():
    print("""
        ***********************************
        * МЕНЮ АВТОРИЗАЦИИ         *
        ***********************************
        * [1] Вход                        *
        * [2] Регистрация                 *
        * [0] Выход                       *
        ***********************************
        """)

    user_input = input("Введите действие: ")

    if user_input.isdigit():
        return int(user_input)
    else:
        print("\nОшибка ввода: введите ответ цифрами 0, 1 или 2.")
        return -1


def login_screen():
    print("""
        ***********************************
        * ОКНО АВТОРИЗАЦИИ         *
        ***********************************
        * Пожалуйста, введите ваши данные *
        ***********************************
        """)

    user_name = input("        ЛОГИН: ")
    user_password = input("        ПАРОЛЬ: ")

    print("    *******************************")

    return user_name, user_password

def logup_screen():
    print("""
        ***********************************
        * ОКНО РЕГИСТРАЦИИ         *
        ***********************************
        * Логин: 3-20 симв.               *
        * Пароль: 4-32 симв.              *
        ***********************************
        """)

    new_user = input("        ПРИДУМАЙТЕ ЛОГИН: ")
    new_password = input("        ПРИДУМАЙТЕ ПАРОЛЬ: ")

    print("    *******************************")

    return new_user, new_password


def registration(login, password):
    with open('database.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{login}:{password}')
        print("""
        ***********************************
        * УСПЕХ: АККАУНТ СОЗДАН!          *
        ***********************************
        * Пользователь успешно сохранен   *
        * в базе данных системы.          *
        ***********************************
        * Теперь вы можете авторизоваться *
        ***********************************
        """)


def validation(login, password):
    if 3 <= len(login) <= 20 and 4 < len(password) <= 32:
        return True

    else:
        print("Ошибка: Несоответствие длины логина или пароля!")
        return False


def check_user(login):
    with open('database.txt', 'r', encoding='utf-8') as file:
        for line in file:
            date = line.strip().split(":")
            if len(date) == 2:
                stored_login = date[0]
                if login == stored_login:
                    print("""
        ***********************************
        * ВНИМАНИЕ: ОШИБКА РЕГИСТРАЦИИ    *
        ***********************************
        * Пользователь с таким логином    *
        * уже зарегистрирован в системе!  *
        ***********************************
        * Пожалуйста, выберите другое имя *
        ***********************************
                        """)
                    return True

    return False


def authorisation(login, password):
    with open('database.txt', 'r', encoding='utf-8') as file:
        for line in file:
            date = line.strip().split(":", 1)
            stored_login = date[0]
            stored_password = date[1]

            if login == stored_login and password == stored_password:
                print("""
    ***********************************
    * ВХОД ВЫПОЛНЕН!           *
    ***********************************
    * Добро пожаловать в систему     *
    ***********************************
                            """)
                return True

        else:
            print("""
        ***********************************
        * ОШИБКА ДОСТУПА           *
        ***********************************
        * Неверный логин или пароль      *
        * Попробуйте еще раз             *
        ***********************************
            """)
            return False


     #  Основной код
if __name__ == "__main__":
     #  Вызов экрана приветствия
     try:
        while True:
            selection = hello_screen()

         #  Выбор ответа от пользователя

            if selection == 1: #  Экран входа пользователя
                print("\nПереход к авторизации...")
                login, password = login_screen()
                if validation(login, password):
                    authorisation(login, password)

            elif selection == 2: #  Экран регистрации нового пользователя
                print("\nПереходим к регистрации...")
                login, password = logup_screen()
                if validation(login, password): #  Валидация
                    if not check_user(login): #  Проверка на уже существующего пользователя
                        registration(login, password)
                    else:
                        selection = -1
                        hello_screen()

            elif selection == 0:
                print("\nЗавершение работы...")
                break
            else:
                continue
     except KeyboardInterrupt:
         print("\nПрограмма была внезапно прервана...")







