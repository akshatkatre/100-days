from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

# id *
# title *
# year *
# description *
# rating *
# ranking *
# review *
# img_url


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    ranking = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String(2000), unique=False, nullable=False)
    img_url = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return f'title {self.title}; year {self.year}; ' \
               f'rating {self.rating}; ranking {self.ranking}'


class EditForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    id = HiddenField('id')
    submit = SubmitField('Submit')


@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    print(movies)
    return render_template("index.html", movies=movies)


@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    form = EditForm(id=id)
    if form.validate_on_submit():
        print("Movie data to be updated...")
        print(form.rating.data, form.review.data)
        movie_id = request.form['id']
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = request.form['rating']
        movie_to_update.review = request.form['review']
        db.session.commit()
        movies = db.session.query(Movie).all()
        return render_template("index.html", movies=movies)
    print("Inside edit ratings")
    print(id)
    movie_id = id
    movie_to_update = Movie.query.get(movie_id)
    form.id = movie_id
    return render_template('edit.html', movie=movie_to_update, form=form)


@app.route("/delete/<id>")
def delete_movie(id):
    print("Inside Delete")
    movie_id = id
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return render_template('index.html', movies=db.session.query(Movie).all())


if __name__ == '__main__':
    app.run(debug=True)
