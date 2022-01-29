from turtle import Turtle

PLAYERS = {
    "p1": (-200, 200),
    "p2": (200, 200),
    "bounces": (0, -230),
    "final": (0,0)
}


class Score(Turtle):

    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setpos(PLAYERS[player])
        self.score = 0
        if player == "bounces":
            self.player = "bounces"
        else:
            self.player = ""
        self.show_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def show_score(self):
        if self.player == "bounces":
            self.write(f"TOTAL HITS: {self.score}", align="center",font=('Arial', 10, 'normal'))
        else:
            self.write(f"{self.score}", align="center", font=('Arial', 25, 'normal'))

    def show_winner(self, winner):
        self.clear()
        self.write(f"{winner} is the winner!", align="center", font=('Arial', 40, 'normal'))

