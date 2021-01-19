from flask import Flask, render_template, request
from common import emailer

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['post'])
def do_login():
    print("/login method invoked...")
    name = request.form['name_inp']
    password = request.form['password_inp']
    return f'<h1>{name} your password is {password}</h1>'


@app.route('/contact', methods=['get'])
def contact_page():
    return render_template("contact.html")


@app.route('/contact', methods=['post'])
def process_contact():
    print("/contact method invoked...")
    name = request.form['name_inp']
    email = request.form['email_inp']
    message = request.form['message_inp']
    email_message = f'Name: {name}\n' \
                    f'Email: {email}\n' \
                    f'Message: {message}'
    # print(name, email, message)
    print(email_message)
    print("sending message...")
    emailer.send_email(email_subject="New Contact!", message_body=email_message)
    return render_template("contact.html", message_processed=True)


if __name__ == "__main__":
    app.run(debug=True)
