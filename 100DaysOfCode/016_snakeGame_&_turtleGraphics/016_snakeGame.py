from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey7")
screen.title("EJ's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Movement
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


def replay():
    response = screen.textinput("Replay?", "Would you like to play again? Type 'y' or 'n'.")

    if response == 'y':
        game_on = True
    else:
        game_on = False

    return game_on


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect moving over food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    # Detect hitting wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        game_on = replay()

    # Detect hitting tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            game_on = replay()


screen.exitonclick()
