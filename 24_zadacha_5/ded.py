from garden import Garden
from potato import Potato


class Ded:

    def __init__(self, name='Володя', active=True):
        self.active = active
        self.name = name

    def auto_work(self, some_garden, some_warehouse, days):
        phrase = ''
        while days > 0:
            if self.active:
                for potato in some_garden.my_garden:
                    if potato.stage < 4:
                        if potato.water:
                            potato.grow_up()
                            phrase = '\nСадовник', self.name, ': Сегодня картошка подросла, а я устал, осталось рабочих дней:' + str(days - 1) + '\n'
                            self.active = False
                        else:
                            potato.pour()
                            phrase = '\nСадовник', self.name, ': Сегодня поливал картошу и устал, осталось рабочих дней:' + str(days - 1) + '\n'
                            self.active = False
                    else:
                        phrase = '\nСадовник', self.name, ': сегодня собираю урожай\n'
                        some_warehouse[0] += potato.collect()
                days -= 1
                print(phrase)
            else:
                self.active = True
                days -= 1
                print('Садовник', self.name, ': взял выходной, осталось рабочих дней:', days, '\n')

    def grow_all(self, some_garden):
        if self.active:
            for potato in some_garden.my_garden:
                potato.grow_up()
            self.active = False
        else:
            print('Садовник', self.name, ': я устал, ничего делать не хочу')

    def collect_all(self, some_garden, some_warehouse):
        if self.active:
            for potato in some_garden.my_garden:
                temp = potato.collect()
                print('Картоша {i} была на стадии {s} поэтому за её сбор получаем {n} едениц картошки'.format(
                    i=potato.index,
                    s=potato.stage,
                    n=temp
                ))
                some_warehouse[0] += temp
            self.active = False
        else:
            print('Садовник', self.name, ': я устал, ничего делать не хочу')

    def pour_all(self, some_garden):
        if self.active:
            for potato in some_garden.my_garden:
                if potato.water:
                    potato.stage -= 1
                    print('Картошка', potato.index, 'уже была полита, её состояние ухудшилось')
                else:
                    potato.pour()
            self.active = False
        else:
            print('Садовник', self.name, ': я устал, ничего делать не хочу')

    def sleep(self):
        if self.active:
            print('Садовник', self.name, ': я только проснулся, делом бы заняться')
        else:
            print('Садовник', self.name, ': поспал и отдохнул, могу работать снова')
            self.active = True

    def check(self, some_garden):
        for potato in some_garden.my_garden:
            if potato.water:
                water_state = ' и она полита'
            else:
                water_state = ', но её нужно полить!'
            print('Картошка номер {} имеет состояние роста {}/4'.format(potato.index, potato.stage) + water_state)