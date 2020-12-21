import time
from turtle import Screen
import random
from crossing_game_23.player import Player
from crossing_game_23.car_manager import CarManager
from crossing_game_23.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.up)

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    if player.has_reached_wall():
        scoreboard.update_scoreboard()
        player.go_to_starting_position()
        car_manager.increase_speed()

    if random.randint(1, 6) == 1:
        car_manager.create_car()

    # detect collision
    for car in car_manager.cars:
        if car.distance(player) < 30:
            print('Game Over')
            scoreboard.game_over()
            game_is_on = False

    counter += 1

screen.exitonclick()
