from flask import Flask
from functools import wraps
import random

app = Flask(__name__)


def make_centered(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        tag = "center"
        wrap.__name__ = func.__name__
        return f"<{tag}>" + func(*args, **kwargs) + f"</{tag}>"

    return wrap


correct_answer = random.randint(0, 9)
print(correct_answer)


@app.route('/')
@make_centered
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'


@app.route("/<int:guess>")
@make_centered
def greet(guess):
    if guess not in range(0, 10):
        return '<h1>Only guess numbers between 0 and 9!</h1>'
    elif guess > correct_answer:
        return '<h1>Too high, try again!</h1>' \
               '<img src = "https://media.giphy.com/media/OqAf4TvOhqTqMwRDA5/giphy.gif" width=400>'
    elif guess < correct_answer:
        return '<h1>Too low, try again!</h1>' \
               '<img src = "https://media.giphy.com/media/ZFZLIuWWkr29y/giphy.gif" width=400>'
    elif guess == correct_answer:
        return '<h1>You found me!!</h1>' \
               '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400>'


if __name__ == "__main__":
    app.run(debug=True)
