from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # relationships
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

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


class Event(db.Model):
    __tablename__ = 'events'
    '''
    Event class to define Event items
    '''
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    day = db.Column(db.String(255))
    #time = db.Column(db.String(255))
    location = db.Column(db.String(255))
    price = db.Column(db.Integer)
    owner = db.Column(db.String(255))
    #followers = db.Column(db.Integer)
    #category = db.Column(db.String(255),index = True)

class Contact(db.Model):
    __tablename__ = 'contacts'
    '''
    Event class to define Event items
    '''
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    subject = db.Column(db.String(255))
    message = db.Column(db.Integer)
  

