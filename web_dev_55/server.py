from flask import Flask
import random

RANDOM_NUMBER: int
app = Flask(__name__)


@app.route('/')
def home():
    global RANDOM_NUMBER
    RANDOM_NUMBER = random.randint(0, 9)
    return '<h1>Guess the number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="numbers"/>'


@app.route('/<int:number>')
def validate(number):
    global RANDOM_NUMBER
    print(f'The random number generated is {RANDOM_NUMBER}, your guess {number}')
    if number == RANDOM_NUMBER:
        return '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="numbers"/>'
    elif number < RANDOM_NUMBER:
        return '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="numbers"/>'
    else:
        return '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="numbers"/>'


if __name__ == "__main__":
    app.run(debug=True)
