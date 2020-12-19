from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!",  align=ALIGNMENT, font=FONT)