from venv import create
import auth

class Player:
    def __init__(self, player_name, player_experience, player_level, experience_for_next_level):
        self.player_name = player_name
        self.player_hp = 100
        self.player_experience = player_experience
        self.player_level = player_level
        self.experience_for_next_level = experience_for_next_level

    def player_level_up(self):
        if self.player_experience > self.experience_for_next_level:
            self.player_level += 1

    def experience_list_to_level_up(self):
        return 100 * self.player_level ** 2

    def player_info(self):
        print(f'''
              Имя игрока: {self.player_name}
                 Уровень: {self.player_level}
        Количество опыта: {self.player_experience}       
            ''')
    #
    # def create_new_player(self):
    #     self.player_name = input('Введите имя для своего персонажа: ')
    #     with ManagedFile('list_players.txt') as players:
    #         list_players = [player for player in players.split()]
    #         if self.player_name not in list_players:
    #             players.write(f'{self.player_name}\n')
    #         else:
    #             print("Имя уже занято! Попробуйте другое")
    #             self.create_new_player()


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

auth()




