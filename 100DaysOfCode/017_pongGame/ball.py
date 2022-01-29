from turtle import Turtle
from random import randint, choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.setheading(choice([randint(0,70), randint(110,250), randint(290,359)]))

    def bounce(self, angle, wall):
        self.speed("fastest")
        if wall == "NS":
            self.setheading(360 - angle)
        elif wall == "WE":
            if angle <= 180:
                self.setheading(180 - angle)
            else:
                self.setheading((270 - angle) + 270)

    def move(self, bounces):
        if bounces <= 2:
            self.speed("slow")
        elif bounces <= 4:
            self.speed("normal")
        elif bounces <= 6:
            self.speed("fast")
        else:
            self.speed("fastest")
        self.forward(5)

    def wall(self):
        if abs(self.ycor()) > 240:
            wall = "NS"
        elif abs(self.xcor()) > 410:
            wall = "WE"
        else:
            wall = ""
        return wall

    def remove(self):
        self.hideturtle()
