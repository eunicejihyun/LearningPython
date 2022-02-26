from flask import Flask, render_template
import requests

posts_url = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(posts_url)
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:id>')
def blog(id):
    response = requests.get(posts_url)
    posts = response.json()
    return render_template("blog.html", posts=posts, id=id)


if __name__ == "__main__":
    app.run(debug=True)
