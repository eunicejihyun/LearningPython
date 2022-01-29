from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score


# Screen Setup
screen = Screen()
screen.setup(width=900, height=500)
screen.bgcolor("grey7")
screen.title("PONG by EJ")


p1 = Paddle("p1")
p2 = Paddle("p2")


screen.listen()
screen.onkey(fun=p1.up, key=p1.info["up"])
screen.onkey(fun=p1.down, key=p1.info["down"])

screen.onkey(fun=p2.up, key=p2.info["up"])
screen.onkey(fun=p2.down, key=p2.info["down"])


s1 = Score("p1")
s2 = Score("p2")
bounces = Score("bounces")


while s1.score < 5 and s2.score < 5:

    s1.show_score()
    s2.show_score()

    ball = Ball()
    while True:
        ball.move(bounces.score)

        wall = ball.wall()

        if abs(ball.ycor()) > 240:
            ball.bounce(ball.heading(), wall)
        elif 423 >= abs(ball.xcor()) >= 418 and \
                (abs(p1.paddle.ycor() - ball.ycor()) <= 31 or abs(p2.paddle.ycor() - ball.ycor()) <= 31):
            ball.bounce(ball.heading(), wall)
            bounces.increase_score()
        elif ball.xcor() > 440:
            s1.increase_score()
            ball.remove()
            break
        elif ball.xcor() < -440:
            s2.increase_score()
            ball.remove()
            break

final = Score("final")
if s1.score == 5:
    final.show_winner("Player 1")
else:
    final.show_winner("Player 2")

screen.exitonclick()
