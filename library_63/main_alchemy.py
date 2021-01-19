from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


# db.create_all()

# book1 = Books(name = 'Chambers of secrets', author='JK Rowlings', rating='9.3')
# book2 = Books(name = 'Prisoner of Azkaban', author='JK Rowlings', rating='9.5')
#
# db.session.add(book1)
# db.session.add(book2)
# db.session.commit()

all_books = db.session.query(Books).all()
for book in all_books:
    print(book.id, book.name, book.author, book.rating)


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
        # book = {
        #     "name" : request.form['name'],
        #     "author" : request.form['author'],
        #     "rating" : request.form['rating']
        # }
        # print(book)
        # all_books.append(book)
        print('adding new book...')
        new_book = Books(name=request.form['name'],
                         author=request.form['author'],
                         rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return render_template('index.html', books=db.session.query(Books).all())


@app.route("/delete/<id>")
def delete_book(id):
    book_id = id
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return render_template('index.html', books=db.session.query(Books).all())


@app.route("/edit/<id>/<rating>")
def edit_rating(id, rating):
    print(id, rating)
    book_id = id
    book_to_update = Books.query.get(book_id)
    book_to_update.rating = rating
    db.session.commit()
    return render_template('index.html', books=db.session.query(Books).all())


if __name__ == "__main__":
    app.run(debug=True)
