from turtle import Screen, Turtle
import random

# ej = Turtle(shape="turtle")
# ej.penup()
# ej.color("red")
# ej.goto(x=-230, y=-150)

# # Etch-a-Sketch
# def fwd():
#     ej.forward(10)
#
# def bwd():
#     ej.backward(10)
#
# def clockwise():
#     ej.right(20)
#
# def counter_clockwise():
#     ej.left(20)
#
# def restart():
#     ej.home()
#     ej.clear()
#
#
# screen.listen()
# screen.onkeypress(key="w", fun=fwd)
# screen.onkeypress(key="s", fun=bwd)
# screen.onkeypress(key="a", fun=counter_clockwise)
# screen.onkeypress(key="d", fun=clockwise)
# screen.onkey(key="c", fun=restart)


# # Turtle Race
#
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#
# user_bet = screen.textinput(title="Who will win the race?", prompt="Name the color of the turtle you think will win: ").lower()
# while user_bet not in colors:
#     user_bet = screen.textinput(title="Who will win the race?", prompt="Please type red, orange, yellow, green, blue or purple: ").lower()
#
# all_turtles = []
#
# y_loc = -150
#
# for a in range(6):
#     new_turtle = Turtle(shape ="turtle")
#     new_turtle.penup()
#     new_turtle.color(colors[a])
#     new_turtle.goto(x=-230, y=y_loc)
#     y_loc += 60
#     all_turtles.append(new_turtle)
#
# winning_color = ''
# while winning_color not in colors:
#     for turtle in all_turtles:
#         if turtle.xcor() >= 230:
#             winning_color = (turtle.pencolor())
#             if winning_color == user_bet:
#                 print(f"You got it! The {winning_color} turtle won the race!")
#             else:
#                 print(f"Better luck next time. The {winning_color} turtle won the race.")
#         move = random.randint(0,10)
#         turtle.forward(move)
#

# Snake Game
