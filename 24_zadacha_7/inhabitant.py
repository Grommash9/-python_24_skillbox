from house import House


class Inhabitant:

    def __init__(self, name, home, hunger=50):
        self.name = name
        self.hunger = hunger
        self.home = home
        home.inhabitant_list.append(self)

    def eat_something(self):
        if self.home.refrigerator >= 10:
            self.home.food_taken()
            self.hunger += 10
            print(self.name, ': поел')
        else:
            print(self.name, 'хотел поесть, но в холодильнике пусто')
            self.hunger -= 10

    def go_word(self):
        self.home.money_added()
        self.hunger -= 10
        print(self.name, ': поработал')

    def play(self):
        self.hunger -= 10
        print(self.name, ': поиграл')

    def shopping(self):
        if self.home.nightstand >= 10:
            self.home.food_added()
            self.home.money_taken()
            print(self.name, ': скупился')
        else:
            self.hunger -= 10
            print(self.name, 'хотел скупиться, но в тумбочке нет денег, проголодался пока ходил')

    def die(self):
        self.home.inhabitant_list.remove(self)

    def info(self):
        return '{name}: голод: {hungry}, дома есть {money} денег, в холодильнике сейчас {food} еды'.format(
                name=self.name,
                hungry=self.hunger,
                money=self.home.nightstand,
                food=self.home.refrigerator
        )
