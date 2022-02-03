TXT = "highScore.txt"

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(TXT) as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align='center', font=('Comic Sans', 15, 'italic'))

    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER", move=False, align='center', font=('Comic Sans', 20, 'italic'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(TXT, mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()




