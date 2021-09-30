from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(6)
        self.draw_border()

    def draw_border(self):
        self.penup()
        self.goto(-300, 300)
        self.pendown()
        for _ in range(4):
            self.forward(600)
            self.right(90)
