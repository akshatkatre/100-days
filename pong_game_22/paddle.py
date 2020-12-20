from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(x=x_position, y=y_position)
        self.speed("fastest")
        self.score = 0

    def up(self):
        y_pos = self.ycor()
        x_pos = self.xcor()
        self.goto(y=y_pos + 20, x=x_pos)

    def down(self):
        y_pos = self.ycor()
        x_pos = self.xcor()
        self.goto(y=y_pos - 20, x=x_pos)

    def increase_score(self):
        self.score += 1



