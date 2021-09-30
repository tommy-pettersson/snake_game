from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.new_position = ()
        self.new_random_position()
        self.refresh()

    def refresh(self):
        self.goto(self.new_position)

    def new_random_position(self):
        self.new_position = (random.randint(-280, 280), random.randint(-280, 280))
