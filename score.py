from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align=ALIGN, font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.update_score()
