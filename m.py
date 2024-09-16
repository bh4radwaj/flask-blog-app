from config import *
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    email = db.Column(db.String(20),nullable=False,unique=True)
    uid = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(100),nullable=False,unique=False)
    posts = db.relationship('Post',backref="author",lazy=True)
    prof = db.relationship('Profile',backref="user",lazy=True)
    comments = db.relationship('Comment',backref="author",lazy=True)

    def __repr__(self):
        return f"User('{self.email}','{self.uid}','{self.password}')"

class Profile(db.Model):
    # __tablename__ = "profiles"
    id = db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    prof_img = db.Column(db.String(20),nullable=False,unique=False,default="default.jpg")
    followers = db.Column(db.Integer,nullable=False,unique=False,default=0)
    following = db.Column(db.Integer,nullable=False,unique=False,default=0)
    following_mens = db.Column(db.String(2000),nullable=False,unique=False,default='')
    albums = db.Column(db.String(2000),nullable=False,unique=False,default='')
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)


    def __repr__(self):
        return f"Profile('{self.prof_img}','{self.followers}','{self.following}')"

class Post(db.Model):
    # __tablename__ = "posts"
    id = db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    title = db.Column(db.String(50),nullable=False,unique=False)
    body = db.Column(db.Text(2000),nullable=False,unique=False)
    img = db.Column(db.String(20),nullable=True,unique=False,default="")
    date = db.Column(db.DateTime,nullable=False,unique=False,default=datetime.utcnow)
    likes = db.Column(db.Integer,nullable=False,unique=False,default=0)
    liked = db.Column(db.String(2000),nullable=False,unique=False,default='')
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    comments = db.relationship('Comment',backref="post",lazy=True)


    def __repr__(self):
        return f"Post('{self.title}','{self.body}','{self.date}')"

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    comment = db.Column(db.String(20),nullable=False,unique=False)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    def __repr__(self):
        return f"Comment('{self.comment}')"

