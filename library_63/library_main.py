from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# all_books = [{"name": "pri", "author": "william", "rating": "7"}]
all_books = []

@app.route('/')
def home():
    print(len(all_books), all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    print('Inside add...')
    if request.method == 'GET':
        return render_template('add.html')
    else:
        # name = request.form['name']
        # author = request.form['author']
        # rating = request.form['rating']
        # print(name, author, rating)
        book = {
            "name" : request.form['name'],
            "author" : request.form['author'],
            "rating" : request.form['rating']
        }
        print(book)
        all_books.append(book)
        return render_template('index.html', books=all_books)



if __name__ == "__main__":
    app.run(debug=True)

