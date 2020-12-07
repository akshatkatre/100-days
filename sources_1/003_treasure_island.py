print("Welcome to the treasure island")

direction = input("Do you want to go left or right? ")

if direction == 'right':
    print('Game Over.')
elif direction == 'left':
    activity = input('Do you want to swim or wait? ')
    if activity == 'swim':
        print('Game over.')
    elif activity == 'wait':
        door = input('Which door? Red/Blue/Yellow? ')
        if door == 'Red' or door == 'Blue':
            print('Game over.')
        elif door == 'Yellow':
            print('You win!')
        else:
            print('Wrong option')
    else:
        print('Wrong option')
else:
    print('Wrong option')
