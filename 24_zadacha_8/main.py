import random
from card import Card
import card


def summa_counter(some_list):
    temp_summa = 0
    for any_card in some_list:
        temp_summa += any_card.value
    return temp_summa


def hand_check(some_hand):
    for cards in some_hand:
        print('||', cards.name, '(', cards.value, ')||')


computer_summa = 0
player_summa = 0

card.new_cards_list()

computer_hand = [Card(random.randint(0, card.cards_left())) for _ in range(2)]
player_hand = [Card(random.randint(0, card.cards_left())) for _ in range(2)]

print('\nКарты в вашей руке')
for cards in player_hand:
    player_summa = summa_counter(player_hand)
    print('||', cards.name, '(', cards.value, ')||')

computer_summa = summa_counter(computer_hand)

if computer_summa >= 21:
    print('\nКомпьютер проиграл')
    print('Вот карты, которые были у компьтера')
    hand_check(computer_hand)
    exit()

while True:
    choose = int(input('\nВзять карту или остановиться? (1/0)'))
    if choose == 1:
        player_hand.append(Card(random.randint(0, card.cards_left())))
        player_summa = summa_counter(player_hand)
        print('\nСейчас ваши карты выглядят так')
        hand_check(player_hand)
        if player_summa > 21:
            print('\nВы набарли больше 21 очка и проиграли =(')
            break
    if choose == 0:
        if player_summa > computer_summa:
            print('\nУ вас {} очков, а у компьютера {} очков, вы победили'.format(player_summa, computer_summa))
            break
        elif player_summa == computer_summa:
            print('\nУ вас {} очков, а у компьютера {} очков, ничья'.format(player_summa, computer_summa))
            break
        elif player_summa < computer_summa:
            print('\nУ вас {} очков, а у компьютера {} очков, вы проиграли'.format(player_summa, computer_summa))
            break

print('\nВот карты, которые были у компьтера')
hand_check(computer_hand)
