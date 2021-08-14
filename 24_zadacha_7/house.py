class House:
    refrigerator = 50
    nightstand = 0
    inhabitant_list = []

    def food_taken(self):
        self.refrigerator -= 10

    def money_added(self):
        self.nightstand += 10

    def money_taken(self):
        self.nightstand -= 10

    def food_added(self):
        self.refrigerator += 10
