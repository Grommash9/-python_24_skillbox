import random
from Warrior import WarriorClass

warriors_names = []

with open('names.txt', 'r') as names_file:
    for line in names_file:
        if line.endswith('\n'):
            line = line[:-1]
        warriors_names.append(line)

warriors_list = [WarriorClass(name) for name in warriors_names]
shorter_len = len(warriors_list) - 1

while len(warriors_list) > 1:
    shorter_len = len(warriors_list) - 1
    attack = random.randint(0, shorter_len)
    defence = random.randint(0, shorter_len)
    while attack == defence:
        defence = random.randint(0, shorter_len)

    print('Воин {attack_name} нападает на {defence_name}'.format(
        attack_name=warriors_list[attack].name,
        defence_name=warriors_list[defence].name
    ))
    warriors_list[defence].damage_taken()
    if warriors_list[defence].health_points == 0:
        print(warriors_list[defence].name, 'выбывает из турнира')
        del warriors_list[defence]
print('Победил воин {warrior_name} у него оставалось {hp_left} здоровья'.format(
    warrior_name=warriors_list[0].name,
    hp_left=warriors_list[0].health_points
))
