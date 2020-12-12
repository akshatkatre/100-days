from art import logo, vs
from game_data import data
import random

# print(random.choice(data))

# print logo
print(logo)

# Function getNextDataOption()
def get_next_data_option(choice: dict):
    generated_option : dict = None
    while generated_option == choice or generated_option == None:
        generated_option = random.choice(data)
    return generated_option

def is_user_correct(A, B, user_inp):
    correct_option: str = None
    if A > B:
        correct_option = 'A'
    else:
        correct_option = 'B'
    if correct_option == user_inp:
        return True
    return False

choice_A: dict = get_next_data_option(None)
choice_B: dict = get_next_data_option(choice_A)
is_user_winning = True
user_score = 0

while is_user_winning:
    print(f"\nCompare A: {choice_A['name']}, {choice_A['description']}, from {choice_A['country']}")
    choice_A_count = choice_A['follower_count']
    # print(choice_A_count)
    print(f"\n{vs}\n")
    print(f"Against B: {choice_B['name']}, {choice_B['description']}, from {choice_B['country']}")
    choice_B_count = choice_B['follower_count']
    # print(choice_B_count)
    user_choice = input("Who has more followers? Type 'A' or 'B': " ).upper()
    is_user_winning = is_user_correct(choice_A_count, choice_B_count, user_choice)
    if is_user_winning:
        choice_A = choice_B
        choice_B = None
        user_score += 1
        choice_B = get_next_data_option(choice_A)

print(f"Sorry, that's wrong. Final score {user_score}")


