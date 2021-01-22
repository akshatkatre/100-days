from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import requests
import os
from movies_64.tmdb_data import Tmdb

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
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(2000), unique=False, nullable=True)
    img_url = db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return f'title {self.title}; year {self.year}; ' \
               f'rating {self.rating}; ranking {self.ranking}'


class EditForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    id = HiddenField('id')
    submit = SubmitField('Submit')


class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    movies = db.session.query(Movie).order_by('rating').all()
    print(movies)
    for i in range(len(movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route('/find/<id>')
def find_and_add(id):
    print(f'Inside find_and_id {id}')
    tmdb = Tmdb()
    movie_data = tmdb.get_movie_details(id)
    new_movie = Movie(title=movie_data['title'],
                      year=movie_data['release_date'],
                      description=movie_data['description'],
                      img_url=movie_data['img_url'])
    db.session.add(new_movie)
    db.session.commit()
    movies = db.session.query(Movie).order_by('rating').all()
    print(movies)
    return render_template("index.html", movies=movies)


@app.route("/add", methods=['GET','POST'])
def add_movie():
    print('Inside add_movie method')
    form = AddForm()
    if form.validate_on_submit():
        print("Movie data to be ADDED...")
        print(form.movie_title.data)
        tmdb = Tmdb()
        movie_list = tmdb.get_movie_list(form.movie_title.data)
        return render_template('select.html', movie_list=movie_list)
    return render_template('add.html', form=form)


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
        movies = db.session.query(Movie).order_by('rating').all()
        for i in range(len(movies)):
            # This line gives each movie a new ranking reversed from their order in all_movies
            movies[i].ranking = len(movies) - i
        db.session.commit()
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
