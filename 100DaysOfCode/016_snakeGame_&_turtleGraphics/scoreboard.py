from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align='center', font=('Comic Sans', 15, 'italic'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align='center', font=('Comic Sans', 20, 'italic'))

