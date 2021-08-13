from garden import Garden
from ded import Ded

my_workhouse = [0]
sadovnik_1 = Ded('Володя')

choose = 1
number = int(input('Введите количество картошек: '))
garden = Garden(number)

while choose != 0:
    choose = int(input('\nВыберите действие для садовника '
                       '\n0 - выйти'
                       '\n1 - поспать'
                       '\n2 - поливать'
                       '\n3 - взращивать'
                       '\n4 - собирать урожай'
                       '\n5 - проверить состояние грядки'
                       '\n6 - авто режим: '))
    if choose == 0:
        break
    elif choose == 1:
        sadovnik_1.sleep()
    elif choose == 2:
        sadovnik_1.pour_all(garden)
    elif choose == 3:
        sadovnik_1.grow_all(garden)
    elif choose == 4:
        sadovnik_1.collect_all(garden, my_workhouse)
    elif choose == 5:
        sadovnik_1.check(garden)
    elif choose == 6:
        days = int(input('Сколько дней будет работать дед?: '))
        sadovnik_1.auto_work(garden, my_workhouse, days)

print('\nВсего на вашем складе', my_workhouse, 'картошек')
