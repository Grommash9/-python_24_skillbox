class Potato:
    def __init__(self, index, state=0, water=False):
        self.index = index
        self.stage = state
        self.water = water

    def pour(self):
        self.water = True
        print('Картошка {number} полита успешно'.format(
            number=self.index
        ))

    def grow_up(self):
        if self.stage < 4:
            if self.water:
                self.stage += 1
                self.water = False
                print('Картошка {number} подросла, теперь её стадия созревания {stage}/4'.format(
                    number=self.index,
                    stage=self.stage
                ))
            else:
                print('Картошка {number} не полита, сухое растение не будет расти'.format(
                    number=self.index
                ))
        else:
            print('Картошка переросла и урожай был испорчен')
            self.stage = 0
            self.water = False

    def collect(self):
        if self.stage == 4:
            self.stage = 0
            return 1
        return 0
