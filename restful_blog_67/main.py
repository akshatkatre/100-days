from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime



## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


##WTForm
class EditPostForm(FlaskForm):
    id = HiddenField('id')
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Edit Post")


@app.route('/', methods=['GET'])
def get_all_posts():
    posts = [blog_post.to_dict() for blog_post in
             db.session.query(BlogPost).all()]
    print(posts)
    #return posts
    return render_template("index.html", all_posts=posts)


@app.route("/post", methods=['GET'])
def show_post():
    index = request.args.get("index")
    requested_post: BlogPost= db.session.query(BlogPost).filter(
        BlogPost.id == index).first().to_dict()
    print(requested_post)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=['GET', 'POST'])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        print('Inside POST handler to create new blog post...')
        for fieldname, value in request.form.items():
            print(fieldname, value)
        now = datetime.now()
        new_blog_post = BlogPost(title = request.form['title'],
                                 subtitle = request.form['subtitle'],
                                 author = request.form['author'],
                                 img_url = request.form['img_url'],
                                 body = request.form['body'],
                                 date = now.strftime("%m/%d/%Y, %H:%M:%S"))
        db.session.add(new_blog_post)
        db.session.commit()
        posts = [blog_post.to_dict() for blog_post in
                 db.session.query(BlogPost).all()]
        return render_template("index.html", all_posts=posts)

    return render_template('make-post.html', form=form)


@app.route("/edit", methods=['GET', 'PUT', 'POST'])
def edit_post():
    post_id = request.args.get("post_id")
    blog = BlogPost.query.get(post_id)
    print(blog.to_dict())
    form = EditPostForm(id = blog.id,
                        title = blog.title,
                        subtitle = blog.subtitle,
                        body = blog.body,
                        author = blog.author,
                        img_url = blog.img_url)
    if form.validate_on_submit():
        print('Inside POST handler to editing blog post...')
        for fieldname, value in request.form.items():
            print(fieldname, value)
        now = datetime.now()
        post_to_update = BlogPost.query.get(request.form['id'])
        post_to_update.title = request.form['title']
        post_to_update.subtitle = request.form['subtitle']
        post_to_update.date = now.strftime("%m/%d/%Y, %H:%M:%S")
        post_to_update.body = request.form['body']
        post_to_update.author = request.form['author']
        post_to_update.img_url = request.form['img_url']
        db.session.commit()
        posts = [blog_post.to_dict() for blog_post in
                 db.session.query(BlogPost).all()]
        return render_template("index.html", all_posts=posts)
    return render_template('edit.html', form=form)


@app.route("/delete")
def delete_post():
    print('Inside blog delete')
    post_id = request.args.get("post_id")
    blog_to_delete = BlogPost.query.get(post_id)
    db.session.delete(blog_to_delete)
    db.session.commit()
    posts = [blog_post.to_dict() for blog_post in
             db.session.query(BlogPost).all()]
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)