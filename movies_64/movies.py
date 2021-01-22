from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
        return f'title {self.title}; year {self.year}'

# The below statement will create the Table.
db.create_all()
#
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# book1 = Books(name = 'Chambers of secrets', author='JK Rowlings', rating='9.3')
# book2 = Books(name = 'Prisoner of Azkaban', author='JK Rowlings', rating='9.5')
#
# db.session.add(book1)
# db.session.add(book2)
# db.session.commit()

# db.session.add(new_movie)
# db.session.commit()

# new_movie = Movie(
#     title="2001: A Space Odyssey",
#     year=1968,
#     description="Stanley Kubrick took science fiction cinema in a grandly intelligent new direction with this epic story of man’s quest for knowledge.",
#     rating=6.3,
#     ranking=2,
#     review="2001: A Space Odyssey is a stand-along monument, a great visionary leap, unsurpassed in its vision of man and the universe. It was a statement that came at a time which now looks something like the peak of humanity’s technological optimism.",
#     img_url="https://www2.bfi.org.uk/sites/bfi.org.uk/files/styles/full/public/image/2001-a-space-odyssey-1968-002-00m-rnw-astronaut-adrift_590.jpg?itok=L95TYYCE"
# )

# new_movie = Movie(
#     title="Titanic",
#     year=1997,
#     description="Searching for a lost diamond aboard the wreckage of the great, ill-fated ship, a diver finds a sketch of a young woman wearing the jewel. Amazingly, she is still alive, and recounts the tale of her time on the luxury liner - a tale of grand romance.",
#     rating=5.5,
#     ranking=3,
#     review="We were, of course, all waiting for it to sink. Or at least list alarmingly. We had our snappily punning headlines and our cleverly worded (Mad)man overboard! captions. James Cameron has spent $200 million on a movie and it's a dog. He's finally had it! we chortled. It was all going to be a great deal of fun. Only there's a slight problem. James Cameron has gone and delivered a spectacular, moving, utterly engrossing three-and-a-bit hour epic (stick that on your poster) of the kind they have putatively ceased making any more. Bugger. There go all the albatross gags, then.",
#     img_url="https://cdn.onebauer.media/one/lifestyle-images/celebrity/59d4ac2c07c78ace382c4735/kate-winslet-leonardo-dicaprio-titanic.jpg?quality=50&width=900&ratio=1-1&resizeStyle=aspectfit&format=jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()

all_movies = db.session.query(Movie).all()
for movie in all_movies:
    print(movie.id, movie.title, movie.description, movie.rating)
    print(movie)
