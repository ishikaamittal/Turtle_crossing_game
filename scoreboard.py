from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.goto(0, 270)
        self.hideturtle()
        self.score_display()

    def score_display(self):
        self.goto(-150, 270)
        self.write(f"Score: {self.score}", align="right", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_display()
