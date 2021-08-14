from inhabitant import Inhabitant
from house import House
import random

bakery_street_5 = House()

valera = Inhabitant('Валера', bakery_street_5)
# petya = Inhabitant('Петя', bakery_street_5)


target_day = 365
day = 0

while day < target_day:
    day += 1
    print('\n     Начался', day, 'день: ')
    for inhabitant in bakery_street_5.inhabitant_list:
        if inhabitant.hunger < 0:
            print(inhabitant.name, 'умирает от голода =(')
            inhabitant.die()
            if len(bakery_street_5.inhabitant_list) < 1:
                print('Все жители дома умерли =((')
                day = target_day
            break
        choose = random.randint(1, 6)
        if inhabitant.hunger < 10:
            inhabitant.eat_something()
        elif bakery_street_5.refrigerator < 10:
            inhabitant.shopping()
        elif bakery_street_5.nightstand < 50:
            inhabitant.go_word()
        elif choose == 1:
            inhabitant.go_word()
        elif choose == 2:
            inhabitant.eat_something()
        else:
            inhabitant.play()

    if len(bakery_street_5.inhabitant_list) >= 1:
        print('\n     День закончился, вот состояние жителей дома: ')
        for inhabitant in bakery_street_5.inhabitant_list:
            print('         ', inhabitant.info())

