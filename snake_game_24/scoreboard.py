from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")
DATA_FILE = 'data.txt'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!",  align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score(self.high_score)
        self.score = 0
        self.update_score()

    def get_high_score(self):
        with open(DATA_FILE, 'r') as file_handle:
            return int(file_handle.read())

    def update_high_score(self, current_high_score):
        with open(DATA_FILE, 'w') as file_handle:
            file_handle.write(str(current_high_score))
