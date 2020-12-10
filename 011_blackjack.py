import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = []
computer_hand = []


def get_score(hand: list):
    total = 0
    contains_ace = False
    for i in hand:
        total += i
        if i == 11:
            contains_ace = True
    if total > 21 and contains_ace:
        return total - 10
    return total


continue_playing = True

user_hand = [random.choice(cards), random.choice(cards)]
computer_hand = [random.choice(cards), random.choice(cards)]
another_card = 'y'
game_ended = False
while another_card == 'y':
    print(f'Your cards: {user_hand}, current score: {sum(user_hand)}')
    print(f"computer's first card: {computer_hand[0]}")
    if sum(computer_hand) == 21:
        print('You lose')
        game_ended = True
    elif sum(user_hand) == 21:
        print('You win')
        game_ended = True
    elif sum(user_hand) > 21 and user_hand.count(11) > 0:
        user_hand[user_hand.index(11)] = 1
        if sum(user_hand) > 21:
            print('you lose')
            game_ended = True
        elif sum(user_hand) == 21:
            print('you win')
            game_ended = True
    elif sum(user_hand) > 21 and user_hand.count(11) == 0:
        print('you lose')
        game_ended = True
        break
    else:
        another_card = input('draw another card y or n? : ')
        if another_card == 'y':
            user_hand.append(random.choice(cards))

if not game_ended:
    while sum(computer_hand) < 16:
        computer_hand.append(random.choice(cards))
        if sum(computer_hand) > 21 and computer_hand.count(11) > 0:
            computer_hand[computer_hand.index(11)] = 1

    print(f'user hand: {user_hand}, {sum(user_hand)}')
    print(f'computer hand: {computer_hand}, {sum(computer_hand)}')
    if sum(computer_hand) > 21:
        print('you win')
    elif sum(computer_hand) == 21:
        print('you lose')
    elif sum(computer_hand) == sum(user_hand):
        print('draw')
    elif sum(user_hand) > sum(computer_hand):
        print('you win')
    elif sum(computer_hand) > sum(user_hand):
        print('you lose')
