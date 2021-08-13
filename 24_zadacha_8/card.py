cards_list = []


def new_cards_list():
    suit_list = ['  ♣️', '  ♦️', '  ♥️', '  ♠️']
    cards = {
        'Двойка': 2,
        'Тройка': 3,
        'Четверка': 4,
        'Пять': 5,
        'Шестерка': 6,
        'Семерка': 7,
        'Восьмерка': 8,
        'Девятка': 9,
        'Десятка': 10,
        'Валет': 10,
        'Дама': 10,
        'Король': 10,
        'Туз': 11
    }

    for name, value in cards.items():
        for suit in suit_list:
            cards_list.append([name + suit, value])


def cards_left():
    return len(cards_list) - 1


class Card:

    def __init__(self, number):
        self.name = cards_list[number][0]
        self.value = cards_list[number][1]
        del cards_list[number]




