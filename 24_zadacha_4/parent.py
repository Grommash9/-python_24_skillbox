class Parent:

    def have_grown(self):
        children_index_to_remove = []
        for child_index in range(len(self.child_list)):
            if not self.age - 16 >= self.child_list[child_index].age:
                children_index_to_remove.append(child_index)
        for index in children_index_to_remove:
            print('Ребенок', self.child_list[index].name, 'уже слишком взрослый, он больше во мне не нуждаеться')
            del self.child_list[index]

    def if_have_a_child(self, index):
        if len(self.child_list) < index:
            return False
        return True

    def __init__(self, name='Батя', age=38, child_list=[]):
        self.name = name
        self.age = age
        self.child_list = child_list

    def info(self):
        return ('Меня зовут {name}, мне {age} лет, мои дети: {children}'.format(
            name=self.name,
            age=self.age,
            children=[children.name for children in self.child_list]

        ))

    def calm_down(self, index):
        if self.if_have_a_child(index):
            self.child_list[index].chill_out()
        else:
            return 'У меня нет такого ребенка'

    def feed_up(self, index):
        if self.if_have_a_child(index):
            self.child_list[index].eat()
        else:
            return 'У меня нет такого ребенка'

    def tell_about(self, index):
        if self.if_have_a_child(index):
            return ('Этого моего ребенка зовут {name}, ему {age}, его голод сейчас {eat},'
                    ' его потребность спать сейчас {sleep}'.format(
                name=self.child_list[index].name,
                age=self.child_list[index].age,
                sleep=self.child_list[index].chill,
                eat=self.child_list[index].satiety
            ))
        else:
            return 'У меня нет такого ребенка'
