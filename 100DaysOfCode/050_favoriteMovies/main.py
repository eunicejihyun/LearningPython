from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Creating the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

MOVIE_DB_API_KEY = "YOUR_API_KEY"
MOVIE_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_FIND_URL = "https://api.themoviedb.org/3/movie"
MOVIE_POSTER_URL = "https://image.tmdb.org/t/p/original/"


# Creating a New Table
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(700), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(700))
    img_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


db.create_all()


# Creating a Form to edit the info
class MovieEditForm(FlaskForm):
    rating = StringField('Rate the Movie out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Update')


# Creating a Form to add a Movie
class MovieAddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Add')


@app.route("/")
def home():
    all_movies = Movies.query.order_by(Movies.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    form = MovieEditForm()
    if form.validate_on_submit():
        movie_to_update = Movies.query.get(id)
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = MovieAddForm()
    if form.validate_on_submit():
        title = form.title.data
        response = requests.get(MOVIE_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": title})
        data = response.json()["results"]
        return render_template("select.html", data=data)
    return render_template("add.html", form=form)


@app.route("/delete")
def delete():
    id = request.args.get("id")
    movie_to_delete = Movies.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/find")
def find():
    id = request.args.get("id")
    request_url = f"{MOVIE_FIND_URL}/{id}"
    print(request_url)
    response = requests.get(request_url, params={"api_key": MOVIE_DB_API_KEY})
    data = response.json()
    print(data)

    # Add a record to the table
    new_movie = Movies(
        title=data["title"],
        # The data in release_date includes month and day, we will want to get rid of.
        year=data["release_date"].split("-")[0],
        img_url=f"{MOVIE_POSTER_URL}{data['poster_path']}",
        description=data["overview"]
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=id))


if __name__ == '__main__':
    app.run(debug=True)
