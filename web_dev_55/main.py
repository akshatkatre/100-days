from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f'<b> {function()}</b>'
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f'<em> {function()}</em>'
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f'<u> {function()}</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return '<html><head></head><title>Home</title><body>' \
           '<h1 style="text-align:center">Hello!</h1 ><p>hope you are well!</p>' \
           '<img src="https://media4.giphy.com/media/3oriO0OEd9QIDdllqo/200.webp?cid=ecf05e47xxgmnoarkvp9orpvkdp9g9i8ujjglyoia0jtlrbh&rid=200.webp" alt="kitten"/></body></html>'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Bye!'


@app.route('/user/<name>/<int:emp_no>')
def greet(name, emp_no):
    return f'hello! {name} your employee number is: {emp_no}'


if __name__ == "__main__":
    app.run(debug=True)
