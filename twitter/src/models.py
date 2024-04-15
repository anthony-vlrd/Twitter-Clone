import datetime
from flask_sqlalchemy import SQLAlchemy

#creating a database adapter object using SQLalchemy
db = SQLAlchemy()

#creating a "User" subclass of SQLAlchemy's db.Model class
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tweets = db.relationship('Tweet', backref='user', cascade="all,delete")

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password   

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }


#creating the "Like" subclass (many-to-many relationship) between user and tweets
likes_table = db.Table(
    'likes',
    db.Column(
        'user_id', db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),
    db.Column(
        'tweet_id', db.Integer,
        db.ForeignKey('tweets.id'),
        primary_key=True
    ),
    db.Column(
        'created_at', db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
)


#creating the "Tweet" subclass 
class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(280), nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    liking_users = db.relationship(
        'User', secondary=likes_table,
        lazy='subquery',
        backref=db.backref('liked_tweets', lazy=True)
    )
    
    #creating a constructor method (intended to create tweets)
    def __init__(self, content: str, user_id: int):
        self.content = content
        self.user_id = user_id

    #creating another method to serialize(prepare for transmission) 
    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id
        } 