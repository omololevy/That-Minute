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
  
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        

    def __repr__(self):
        return f'User {self.username}'
    
    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='SET NULL'),nullable = True)
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvotes = db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvotes = db.relationship('Downvote',backref='pitch',lazy='dynamic')
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
       
    @classmethod
    def get_pitches(cls,pitch_category):
        pitches = Pitch.query.filter_by(category=pitch_category).all()
        return pitches
  
    def __repr__(self):
        return f'Pitch {self.pitch}'
    
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255),unique=True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id',ondelete='SET NULL'),nullable = True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='SET NULL'),nullable = True) 
       
    def save_comment(self):
        if self not in db.session:
            db.session.add(self)
            db.session.commit()
        
    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments  
  
    def __repr__(self):
        return f'Comment {self.pitch}'

