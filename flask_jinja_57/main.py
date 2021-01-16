from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=blog_url)
    response.raise_for_status()
    return render_template("index.html", posts=response.json())


@app.route('/post/<int:blog_id>')
def blog_details(blog_id: int):
    print(f'blog id: {blog_id}')
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=blog_url)
    response.raise_for_status()
    data = response.json()[blog_id-1]
    print(data)
    return render_template('post.html', post=data)


if __name__ == "__main__":
    app.run(debug=True)
