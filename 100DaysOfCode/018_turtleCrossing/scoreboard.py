from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.penup()
        self.goto(-190, 260)

    def show_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.clear()
        self.color("crimson")
        self.setx(0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))

