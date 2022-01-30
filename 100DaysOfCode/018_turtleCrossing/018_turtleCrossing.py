from turtle import Turtle, Screen
from boardManager import BoardManager
from carManager import CarManager
from player import Player
from scoreboard import Scoreboard
import time


# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

bm = BoardManager()
cm = CarManager()
sb = Scoreboard()

#Draw Board
time.sleep(0.1)
bm.draw_board()
cm.setup()
sb.show_score()
screen.update()

game_on = True
x = 0.1
while game_on:

    player = Player()

    screen.listen()
    screen.onkeypress(fun=player.move_forward, key="space")

    level_on = True
    loop = 0
    x *= 0.9
    while level_on:

        time.sleep(x)

        if loop % 3 == 0:
            cm.new_car()
        loop += 1

        cm.move_car()

        for car in cm.car_list:
            if abs(player.xcor() - car.xcor()) < 30 and abs(player.ycor() - car.ycor()) < 20:
                level_on = False
                game_on = False
                sb.game_over()
                break

        if player.ycor() >= 280:
            sb.increase_level()
            player.hideturtle()
            level_on = False

        screen.update()

screen.exitonclick()

