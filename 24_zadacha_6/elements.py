from none import EmptyResult


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        temp_tuple = (self.name, other.name)
        for name, result in conformity_list.items():
            if name == temp_tuple or name == temp_tuple[::-1]:
                return result
        return EmptyResult()


class Dirt:

    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        temp_tuple = (self.name, other.name)
        for name, result in conformity_list.items():
            if name == temp_tuple or name == temp_tuple[::-1]:
                return result
        return EmptyResult()


class Dust:

    def __init__(self):
        self.name = 'Пыль'


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        temp_tuple = (self.name, other.name)
        for name, result in conformity_list.items():
            if name == temp_tuple or name == temp_tuple[::-1]:
                return result
        return EmptyResult()


class Meat:

    def __init__(self):
        self.name = 'Мясо'

    def __add__(self, other):
        temp_tuple = (self.name, other.name)
        for name, result in conformity_list.items():
            if name == temp_tuple or name == temp_tuple[::-1]:
                return result
        return EmptyResult()


class Steak:

    def __init__(self):
        self.name = 'Стейк'


class DirtyMeat:

    def __init__(self):
        self.name = 'Грязное мясо'


class DriedMeat:

    def __init__(self):
        self.name = 'Высушенное мясо'


class Lava:

    def __init__(self):
        self.name = 'Лава'


class Lightning:

    def __init__(self):
        self.name = 'Молния'


class Soil:

    def __init__(self):
        self.name = 'Грязь'


class Steam:

    def __init__(self):
        self.name = 'Пар'


class Storm:

    def __init__(self):
        self.name = 'Шторм'


class Water:

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        temp_tuple = (self.name, other.name)
        for name, result in conformity_list.items():
            if name == temp_tuple or name == temp_tuple[::-1]:
                return result
        return EmptyResult()


conformity_list = {
    ('Вода', 'Воздух'): Storm(),
    ('Огонь', 'Вода'): Steam(),
    ('Вода', 'Земля'): Soil(),
    ('Воздух', 'Огонь'): Lightning(),
    ('Воздух', 'Земля'): Dust(),
    ('Огонь', 'Земля'): Lava(),
    ('Мясо', 'Огонь'): Steak(),
    ('Земля', 'Мясо'): DirtyMeat(),
    ('Воздух', 'Мясо'): DriedMeat()

}
