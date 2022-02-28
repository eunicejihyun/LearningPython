from flask import Flask, render_template, request
import requests
import smtplib as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# EMAIL PORTION _________________________________________________________________________
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


# _________________________________________________________________________


app = Flask(__name__)

posts = requests.get("https://api.npoint.io/7908bafaebaf1da6f559").json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:id>')
def blog(id):
    requested_post = None
    for post in posts:
        if post['id'] == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


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


if __name__ == "__main__":
    app.run(debug=True)
