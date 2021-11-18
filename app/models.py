from . import db

class Event(db.Model):
    __tablename__ = 'events'
    '''
    Event class to define Event items
    '''
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    #time = db.Column(db.String(255))
    location = db.Column(db.String(255))
    price = db.Column(db.Integer)
    owner = db.Column(db.String(255))
    #followers = db.Column(db.Integer)
    #category = db.Column(db.String(255),index = True)
        