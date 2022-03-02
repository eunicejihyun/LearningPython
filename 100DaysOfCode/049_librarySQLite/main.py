from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, InputRequired, URL
from flask_bootstrap import Bootstrap
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# ##### SQLite DATABASE _______________________________________________________________________________________________
# db = sqlite3.connect("books.db")
# cursor = db.cursor()
#
# cursor.execute("INSERT INTO books VALUES(934999, 'PL?34?', 'J. K. Rowling', '94049')")
# db.commit()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# def add_book(book_id, title, author, rating):
#     cursor.execute(f"INSERT INTO books VALUES({book_id}, {title}, {author}, {rating})")
#     db.commit()


# ##### FLASK APP _______________________________________________________________________________________________
app = Flask(__name__)
app.config['SECRET_KEY'] = 'nglidkwhatthisdoes'
Bootstrap(app)

# ##### SQL Alchemy ________________________________________________________________________________________________
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# ##### Books Data _______________________________________________________________________________________________
# all_books = []
rating_options = ['⭐⭐⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐', '⭐⭐', '⭐']


class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Author Name', validators=[DataRequired()])
    rating = SelectField('Book Rating', choices=rating_options, validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        title = form.name.data
        author = form.author.data
        rating = form.rating.data

        # book_data = {"title": form.name.data,
        #              "author": form.author.data,
        #              "rating": form.rating.data}
        # all_books.append(book_data)
        new_book = Books(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return home()

    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
