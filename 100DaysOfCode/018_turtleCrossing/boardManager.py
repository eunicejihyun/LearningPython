from turtle import Turtle
import time


class BoardManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.speed("fastest")

    def draw_board(self):
        self.shapesize(stretch_wid=2, stretch_len=30)

        # Make Sand
        self.goto(0, -280)
        self.color("beige")
        self.stamp()

        # Make Water
        self.goto(0, 280)
        self.color("lightskyblue")
        self.stamp()

        # Make Street Lines
        self.color("slategrey")
        self.setheading(180)
        self.width(2)
        y = -220
        while y <= 220:
            self.goto(300, y)
            for i in range(0, 15):
                self.forward(25)
                self.pendown()
                self.forward(15)
                self.penup()
            y += 40

