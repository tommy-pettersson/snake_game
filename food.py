from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, segments):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.refresh(segments)

    def refresh(self, segments):
        new_location = self.random_location()
        while not self.location_ok(new_location, segments):
            new_location = self.random_location()
        self.goto(new_location)

    def random_location(self):
        return (random.randint(-280, 280), random.randint(-280, 280))

    def location_ok(self, location, segments):
        clear_snake = True
        for segment in segments:
            if segment.distance(location) < 40:
                clear_snake = False
        return clear_snake
