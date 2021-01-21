import sqlite3

db = sqlite3.connect("movies.db")
cursor = db.cursor()

# id
# title
# year
# description
# rating
# ranking
# review
# img_url

# Create table
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "year INTEGER NOT NULL, "
#                "description varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL, "
#                "ranking FLOAT NOT NULL, "
#                "review varchar(2000) NOT NULL, "
#                "img_url varchar(2000) NOT NULL "
#                ")")


