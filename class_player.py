
class Player:
    instance_count = 0

    def __init__(self, name,age, height, weight):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight
        self._team = None
        Player.instance_count +=1

    def __str__(self):
       return f'This is {self._name}'

    def get_age(self):
        print(f'{self._name} age is {self._age}')

    def get_height(self):
        print(f'{self._name} height is {self._height}')

    def get_weihgt(self):
        print(f'{self._name} weight is {self._weight}')


#3) Реализовать класс Команда, который бы имел возможность добавлять нового игрока в команду.
# Имел атрибуты экземпляра player, name.
#4) реализовать метод который бы выводил всех игроков команды. Team().name

class Team:
    name = {}

    def __init__(self, team_name, *players):
        self.team_name = team_name
        self._all_team = []
        self.player = self.new_team(*players)

    def new_team(self, *players):
        for player in players:
            if isinstance(player, Player):
                self.player = player
                player._team = self.team_name
                self._all_team.append(self.player)
                Team.name[self.team_name] = self.get_players_team()

    def get_players_team(self):
        return [player._name for player in self._all_team]

    def __str__(self):
        return f'{self.team_name} : {self.get_players_team()}'

player1 = Player('Vasya', 35, 176, 78)
player2 = Player('Petya', 36, 200, 100)

bull = Team('Bull', player2, player1)

player4 = Player('Andy', 37, 176, 80)
bull.new_team(player4)
print('------')
chicago = Team('Chicago', player1)
print(Team.name)
print(bull)
print(chicago)