from turtle import Turtle, Screen
from pandas import *

screen = Screen()
screen.title("US States Game")

# Add turtle shape as US map
image = "blank_states_img.gif"
screen.addshape(image)

Turtle(image)

# Helper turtle will write state names.
helper = Turtle()
helper.penup()
helper.hideturtle()
helper.speed(0)



df = read_csv("50_states.csv")

title = "Name all the states!"
prompt = "Name a state:"

all_states = list(df["state"])


guessed_states = []
while len(guessed_states) < 50:
    guess = screen.textinput(title=title, prompt=prompt).title().strip()
    print(guess)

    if guess == "Exit":

        helper.color("red")

        for unguessed_state in all_states:
            if unguessed_state not in guessed_states:
                data = df[df.state == unguessed_state]
                helper.goto(int(data.x), int(data.y))
                helper.write(data.state.item(), align="center")
        title = f"Take a screenshot now!"
        break

    elif guess in guessed_states:
        prompt = "You already guessed that, silly! Try again."

    elif guess in all_states:
        data = df[df.state == guess]
        helper.goto(int(data.x), int(data.y))
        helper.write(guess, align="center")
        guessed_states.append(guess)
        title = f"{len(guessed_states)}/50 States Correct!"
        prompt = "Name another state state:"

    else:
        prompt = "Never heard of that state before! Try again."



screen.exitonclick()






# # Find the coordinates of each state
# def get_mouse_coor(x, y):
#     print(x,y)
# onscreenclick(get_mouse_coor)
# screen.mainloop()