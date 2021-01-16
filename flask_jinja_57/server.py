from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    number = random.randint(1, 10)
    now = datetime.datetime.now()
    current_year = now.year

    return render_template("index_old.html", number=number, current_year=current_year)


@app.route("/guess/<name>")
def guess(name: str):
    print(f"name: {name}")
    input_parameters = {
        "name": name
    }

    response = requests.get(url="https://api.agify.io", params=input_parameters)
    response.raise_for_status()
    # print(response.text)
    age = response.json()['age']
    print(age)

    response = requests.get(url="https://api.genderize.io", params=input_parameters)
    response.raise_for_status()
    gender = response.json()['gender']
    print(gender)
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<int:num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=blog_url)
    response.raise_for_status()
    blog_data = response.json()
    print(blog_data)
    return render_template("blog.html", posts = blog_data)


if __name__ == "__main__":
    app.run(debug=True)
