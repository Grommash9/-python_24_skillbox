from potato import Potato


class Garden:

    def __init__(self, potato_count=5, state=0, water=True):
        self.state = state
        self.water = water
        self.my_garden = [Potato(x, state, water) for x in range(potato_count)]
