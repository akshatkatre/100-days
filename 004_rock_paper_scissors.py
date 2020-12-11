rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
options = [rock, paper, scissors]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

system_choice = random.randint(0,2)
print(options[user_choice])
print('Computer chose:')
print(options[system_choice])

if user_choice == system_choice:
    print('its a draw')
elif user_choice == 0 and system_choice == 2:
    print('you win')
elif user_choice ==1 and system_choice == 0:
    print('you win')
elif user_choice == 2 and system_choice == 1:
    print('you win')
else:
    print('you lose')