class Child:
    def __init__(self, name='Малой', age=1, chill=True, satiety=True):
        self.name = name
        self.age = age
        self.chill = chill
        self.satiety = satiety

    def eat(self):
        self.satiety = False
        print(self.name, 'поел, теперь его сосояние голода: ', self.satiety)

    def chill_out(self):
        self.chill = False
        print(self.name, 'почилил, теперь его сосояние чилла: ', self.chill)
