from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from flask_gravatar import Gravatar
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from forms import PostForm, RegistrationForm, LoginForm, CommentForm
from functools import wraps

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
app.config['SECRET_KEY'] = '\xfa7\xe0\xdeA\x98\xfc9\xd1\x03\xdfR\xf9\x9f\xd3[\x0eW\xe2\xfc\xec>i\xde'
ckeditor = CKEditor(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
# For getting random commenter images
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CONNECT TO THE SQLALCHEMY DATABASE ##################################################################################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE DATABASE TABLE ###########################################################################################
class BlogPost(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="commenter")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    commenter_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    commenter = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    post = relationship("BlogPost", back_populates="comments")


db.create_all()


# ENSURE ONLY ADMIN CAN ACCESS SPECIFIC PAGES ########################################################################
def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return function(*args, **kwargs)

    return decorated_function


# FLASK SETUP ########################################################################################################
@app.route('/')
def get_all_posts():
    # V2: Get blogs posts via posts.db ################################################################################
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        user = db.session.query(User).filter_by(email=request.form.get("email")).first()
        if user:
            flash('That email is already registered in our database.')
            return redirect(url_for('login'))
        else:
            new_user = User(
                name=request.form.get("name"),
                email=request.form.get("email"),
                password=generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.session.query(User).filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('get_all_posts'))
            else:
                flash('Password incorrect.')
                return redirect(url_for('login'))
        else:
            flash('That email is not registered in our database.')
            return redirect(url_for('login'))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    form = CommentForm()
    requested_post = db.session.query(BlogPost).get(post_id)
    if form.validate_on_submit():
        new_comment = Comment(
            text=form.comment.data,
            post_id=post_id,
            commenter_id=current_user.id
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template("post.html", post=requested_post, form=form)


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
@admin_only
def create_new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y"),
            author_id=current_user.id
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route('/delete/<int:post_id>')
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route('/delete/<int:post_id>/<int:comment_id>')
@login_required
def delete_comment(comment_id, post_id):
    comment_to_delete = Comment.query.get(comment_id)
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for('show_post', post_id=post_id))


if __name__ == "__main__":
    app.run(debug=True)
