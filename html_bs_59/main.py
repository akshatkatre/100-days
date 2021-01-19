from flask import Flask, render_template, request
import requests
from common import emailer

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/contact', methods=['get'])
def contact_page():
    return render_template("contact.html")


@app.route('/contact', methods=['post'])
def process_contact():
    print("/contact method invoked...")
    name = request.form['name_inp']
    email = request.form['email_inp']
    phone = request.form['phone_inp']
    message = request.form['message_inp']
    email_message = f'Name: {name}\n' \
                    f'Email: {email}\n' \
                    f'Phone: {phone}\n' \
                    f'Message: {message}'
    # print(name, email, message)
    print(email_message)
    print("sending message...")
    emailer.send_email(email_subject="New Contact!", message_body=email_message)
    return render_template("contact.html", message_processed=True)

if __name__ == "__main__":
    app.run(debug=True)
