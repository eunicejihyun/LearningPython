from flask import Flask, render_template
import random
from datetime import datetime
import requests

genderize = "https://api.genderize.io"
agify = "https://api.agify.io"

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    params = {"name": name}
    response = requests.get(genderize, params=params)
    gender = response.json()["gender"]
    response2 = requests.get(agify, params=params)
    age = response2.json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
