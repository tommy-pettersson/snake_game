from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.goto(0, 325)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()
        with open("data.txt", "w") as data:
            data.write(f"{self.high_score}")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
