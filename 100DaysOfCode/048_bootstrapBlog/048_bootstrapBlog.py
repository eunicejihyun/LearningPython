from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import smtplib as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

# CONTACT FORM ########################################################################################################
# Sends an email to your e-mail address with the message and contact info of the sender

FROM_GMAIL = "your email"
PASSWORD = "your password"
EMAIL_LIST = ["your list of emails"]


def send_email(text):
    message = MIMEMultipart("alternative")
    message['Subject'] = "New message from your blog!"
    message['From'] = FROM_GMAIL
    message['To'] = ", ".join(EMAIL_LIST)

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    with s.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_GMAIL, password=PASSWORD)
        connection.send_message(msg=message,
                                from_addr=FROM_GMAIL,
                                to_addrs=EMAIL_LIST)


# # V1: Gets a json of the blog posts using the requests module ########################################################
# import requests
# posts = requests.get("https://api.npoint.io/7908bafaebaf1da6f559").json()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'notEntirelySureWhatThisDoes'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO THE SQLALCHEMY DATABASE ##################################################################################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE DATABASE TABLE ###########################################################################################
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# SETUP WTFORM ########################################################################################################
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# FLASK SETUP ########################################################################################################
@app.route('/')
def all_posts():
    # V2: Get blogs posts via posts.db ################################################################################
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:id>')
def blog(id):
    requested_post = None
    for post in posts:
        if post.id == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        email_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        send_email(email_content)
        return "Successfully sent your message"
    else:
        return render_template("contact.html")


@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post_data = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post_data)
        db.session.commit()
        return redirect(url_for('all_posts'))
    return render_template("make-post.html", form=form)


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
