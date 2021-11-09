from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')
    upvotes = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvotes = db.relationship('Downvote',backref='user',lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
  
    
    