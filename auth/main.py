from pyexpat.errors import messages

import auth
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


class Player:
    def __init__(self, characters, user_input, target_player):
        self.target_player = target_player
        # self.player_hp = 100
        # self.player_experience = player_experience
        # self.player_level = player_level
        # self.experience_for_next_level = experience_for_next_level
        self.characters = characters
        self.user_input = user_input

    def _draw_box(self, title, messages, width = 40):
        """Вспомогательный метод для отрисовки рамок (DRY)."""
        if isinstance(messages, str):
            messages = textwrap.wrap(messages, width - 4)

        inner_width = width - 4

        print('\n' + '*' * width)
        print(f'* {title.upper():^{inner_width}} *')
        print('*' * width)

        for msg in messages:
            # Если строка слишком длинная, она не сломает рамку
            print(f"* {msg:<{inner_width}} *")

        print("*" * width)

    # def player_level_up(self):
    #     if self.player_experience > self.experience_for_next_level:
    #         self.player_level += 1
    #         return self.player_level

    def character_selection(self):
        message = [str(character) for character in self.characters] if self.characters else ['Список персонажей пуст']
        if message == 'Список персонажей пуст':
            self._draw_box(
                title='СПИСОК ПЕРСОНАЖЕЙ ПУСТ',
                messages='Хотите создать персонажа? y/n'
            )

            return -1

        else:
            self._draw_box(
                title='МЕНЮ ВЫБОРА ПЕРСОНАЖА',
                messages = message
            )

            self.user_input = input('Введите цифру: ')
            if self.user_input.isdigit():
                return int(self.user_input)
            else:
                self._draw_box('ОШИБКА', 'ввода: введите ответ цифрами: 0, 1 или 2.')
                return -1




    def experience_list_to_level_up(self):
        return 100 * self.player_level ** 2

    def player_info(self):
        self._draw_box(
            title='ИНФОРМАЦИЯ О ПЕРСОНАЖЕ',
            messages = [
                f'Игрок: {self.player_name}',
                f'Уровень: {self.player_level}',
                f'Количество опыта: {self.player_experience}'
                ]
            )

    def create_new_player(self):
        self.player_name = input('Введите имя для своего нового персонажа: ')
        with ManagedFile(filename='list_players.txt', mode='a') as players:
            characters = [character for character in characters.split()]
            if self.player_name not in characters:
                players.write(f'{auth.User.login}:{self.player_name}\n')
            else:
                print("Имя уже занято! Попробуйте другое")
                self.create_new_player()

    def hello_screen(self):
        if


if __name__ == "__main__":
    # play_game = auth.User('', '', -1)
    # if play_game.start_session():
    #     pass
    lobby_game = Player('', -1, '')
    lobby_game.character_selection()



