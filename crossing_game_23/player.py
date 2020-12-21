from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.go_to_starting_position()

    def up(self):
        self.forward(distance=MOVE_DISTANCE)

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)

    def has_reached_wall(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False
