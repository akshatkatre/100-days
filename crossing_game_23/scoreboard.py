from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "Center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score: int = None
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.score is None:
            self.score = 0
        else:
            self.score += 1
        self.clear()
        self.goto(-240, 275)
        self.write(f"Level: {self.score}", move=False, align=ALIGNMENT, font=FONT )

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!",  align=ALIGNMENT, font=FONT)