from sqlalchemy.orm import relationship
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from sqlalchemy import desc



class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    fname = db.Column(db.String(255), index = True)
    lname = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True)
    username = db.Column(db.String(40))
    password_secure  = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='author', lazy='dynamic')        
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute.')
       
    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    def __repr__(self):
        return f'User{self.username}'
    
    @login_manager.user_loader
    def load_user(get_id):
        return User.query.get(get_id)


class Pitch(db.Model):
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key =  True)
    pitch = db.Column(db.Text)
    author = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key =  True)
    comments = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
   
