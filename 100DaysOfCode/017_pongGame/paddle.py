from turtle import Turtle

MOVE_DISTANCE = 30

PLAYERS = {
    "p1": {
        "name": "PLAYER 1",
        "x_loc": -430,
        "color": "hotpink",
        "up": "w",
        "down": "s"
    },
    "p2": {
        "name": "PLAYER 2",
        "x_loc": 430,
        "color": "aqua",
        "up": "Up",
        "down": "Down"
    }
}


class Paddle:

    def __init__(self, player):
        self.info = PLAYERS[player]
        self.paddle = Turtle("square")
        self.paddle.color(self.info["color"])
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=0.5, stretch_len=3)
        self.paddle.setheading(90)
        self.paddle.setx(self.info["x_loc"]*4/5)
        self.paddle.write(self.info["name"], align="center", font=('Arial', 15, 'normal'))
        self.paddle.setx(self.info["x_loc"])
        self.paddle.speed("fastest")

    def up(self):
        if self.paddle.ycor() <= 200:
            self.paddle.clear()
            self.paddle.forward(MOVE_DISTANCE)

    def down(self):
        if self.paddle.ycor() >= -200:
            self.paddle.clear()
            self.paddle.backward(MOVE_DISTANCE)




