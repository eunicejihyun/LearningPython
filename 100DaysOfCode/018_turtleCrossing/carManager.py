from turtle import Turtle
from random import choice, randint

COLORS = ["coral", "aquamarine", "lavender"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = []

for y in range(-260, 260):
    if y % 40 == 0:
        Y_POSITIONS.append(y)

recent_y = []


class CarManager:

    def __init__(self):
        self.car_list = []

    def setup(self):
        for i in range(15):
            self.new_car()
            self.car_list[i].setx(randint(-20, 310))

    def prevent_overlap(self):
        y = choice(Y_POSITIONS)
        while y in recent_y:
            y = choice(Y_POSITIONS)
        recent_y.append(y)
        if len(recent_y) > 6:
            del recent_y[0]
        return y

    def new_car(self):
        car = Turtle("square")
        car.hideturtle()
        car.color(choice(COLORS))
        car.penup()
        car.speed("normal")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.setheading(180)
        car.setposition(305, self.prevent_overlap())
        car.showturtle()
        self.car_list.append(car)

    def move_car(self):
        if len(self.car_list) > 100:
            del self.car_list[0: 10]

        for i in range(len(self.car_list)):
            if self.car_list[i].xcor() > -320:
                self.car_list[i].forward(MOVE_INCREMENT)
