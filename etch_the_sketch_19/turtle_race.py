from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(prompt='Choose the color of you turtle', title='Make your bet').lower()
print(user_bet)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []

start_y = 150
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, start_y)
    turtle_list.append(new_turtle)
    start_y -= 50


is_race_on = False

if user_bet:
    is_race_on = True
winner: str = None

while is_race_on:
    movement = random.randint(0, 10)
    t = random.choice(turtle_list)
    t.forward(movement)
    if t.xcor() > 230:
        winner = t.pencolor()
        print()
        is_race_on = False
        break

if winner == user_bet:
    print(f'The winner is {winner}, You win!')
else:
    print(f'The winner is {winner}, You lose.')


screen.exitonclick()