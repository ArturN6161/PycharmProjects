import textwrap


class ManagedFile:
    """Контекстный менеджер для безопасной работы с БД."""
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Устанавливаем кодировку utf-8 для корректного чтения кириллицы
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class User:
    def __init__(self, login, password, user_input):
        self.login = login
        self.password = password
        self.user_input = user_input

    def _draw_box(self, title, messages, width = 40):
        """Вспомогательный метод для отрисовки рамок (DRY)."""
        if isinstance(messages, str):
            messages = textwrap.wrap(messages, width - 4)

        inner_width = width - 4

        print('\n' + '*' * width)
        print(f'*{title.upper():^{inner_width}}  *')
        print('*' * width)

        for msg in messages:
            # Если строка слишком длинная, она не сломает рамку
            print(f"* {msg:<{inner_width}} *")

        print("*" * width)


    def hello_screen(self):
        self._draw_box(
            title='МЕНЮ АВТОРИЗАЦИИ',
            messages = [
                "[1]    Вход",
                "[2]    Регистрация",
                "[0]    Выход"
            ]
        )

        self.user_input = input('Введите цифру: ')

        if self.user_input.isdigit():
            return int(self.user_input)
        else:
            self._draw_box('ОШИБКА', 'ввода: введите ответ цифрами 0, 1 или 2.')
            return -1

    def login_screen(self, width = 40):
        self._draw_box(
            'ОКНО АВТОРИЗАЦИИ',
            'Пожалуйста, введите ваши данные'
        )

        self.login = input('  ЛОГИН: ' )
        self.password = input('  ПАРОЛЬ: ')

        print('*' * width)

        return self.login, self.password

    def logup_screen(self):
        self._draw_box(
        title='ОКНО РЕГИСТРАЦИИ',
        messages=['Логин: 3-20 симв.','Пароль: 4-32 симв.']
        )

        new_user = input('  ЛОГИН: ')
        new_password = input('  ПАРОЛЬ: ')

        return new_user, new_password

    def registration(self):
        with ManagedFile(filename='data users.txt', mode='a') as file:
            file.write(f'\n{self.login}:{self.password}')
            self._draw_box(
                title="Успех: Аккаунт создан!",
                messages=[
                    "Пользователь сохранен в базе.",
                    "Теперь вы можете авторизоваться"
                ]
            )

    def validation(self):
        if 3 <= len(self.login) <= 20 and 4 < len(self.password) <= 32:
            return True

        else:
            self._draw_box(
                'ОШИБКА',
                'Несоответствие длины логина или пароля!')
            return False


    def check_user(self):
        try:
            with ManagedFile(filename='data users.txt', mode='r') as file:
                for line in file:
                    data = line.strip().split(':', 1)
                    stored_login = data[0]
                    if self.login == stored_login:
                        self._draw_box(
                            'ВНИМАНИЕ: ОШИБКА РЕГИСТРАЦИИ',
                            'Пользователь с таким логином уже зарегистрирован в системе!'
                        )
                        return True
        except FileNotFoundError:
            self._draw_box(
                'КРИТИЧЕСКАЯ ОШИБКА',
                'Файл базы данных не обнаружен в системе.'
            )

        return False


    def authorisation(self, login, password):
        try:
            with ManagedFile(filename='data users.txt', mode='r') as file:
                for line in file:
                    data = line.strip().split(':', 1)
                    stored_login = data[0]
                    stored_password = data[1]

                    if login == stored_login and password == stored_password:
                        self._draw_box(
                            'ВХОД ВЫПОЛНЕН!',
                            'Добро пожаловать в систему.'
                        )

                        return True

                else:
                    self._draw_box(
                        'ОШИБКА ДОСТУПА',
                        'Неверный логин или пароль. Попробуйте еще раз!'
                    )

                    return False
        except FileNotFoundError:
            self._draw_box(
                        'КРИТИЧЕСКАЯ ОШИБКА',
                        'Файл базы данных не обнаружен в системе.'
                )


    def start_session(self):
         #  Вызов экрана приветствия
         try:
            while True:
                selection = self.hello_screen()

             #  Выбор ответа от пользователя

                if selection == 1: #  Экран входа пользователя
                    print('\nПереход к авторизации...')
                    login, password = self.login_screen()
                    if self.validation():
                        if self.authorisation(login, password):
                            break

                elif selection == 2: #  Экран регистрации нового пользователя
                    print('\nПереходим к регистрации...')
                    self.login, self.password = self.logup_screen()
                    if self.validation(): #  Валидация
                        if not self.check_user(): #  Проверка на уже существующего пользователя
                            self.registration()
                        else:
                            self.hello_screen()

                elif selection == 0:
                    print('\nЗавершение работы...')
                    break
                else:
                    continue
         except KeyboardInterrupt:
             print('\nПрограмма была внезапно прервана...')


    #  Основной код
if __name__ == '__main__':
    try:
        app = User(login='', password='', user_input=-1)
        app.start_session()
    except KeyboardInterrupt:
        print("\nИгра прервана пользователем.")




