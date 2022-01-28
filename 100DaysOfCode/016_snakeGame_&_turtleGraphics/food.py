from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("orchid")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_loc = random.randint(-280, 280)
        y_loc = random.randint(-280, 280)
        self.goto(x_loc, y_loc)


