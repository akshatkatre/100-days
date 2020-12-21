from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# CAR_START_POSITIONS = [(300, 250), (300, 200), (300, 150), (300, 100), (300, 50), (300, 0), (300, -50), (300, -100),
# (300, -150), (300, -200)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        # new_car.goto(random.choice(CAR_START_POSITIONS))
        new_car.goto((300, random.randint(-250, 250)))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT







