class WarriorClass:
    health_points = 100

    def __init__(self, name='nameless'):
        health_points = 100
        self.name = name

    def info(self):
        print('Воин {} имеет {} здоровья'.format(self.name, self.health_points))

    def damage_taken(self):
        self.health_points -= 20
        print(f'Воин {self.name} получил 20 урона, его текущий запас здоровья {self.health_points}')
