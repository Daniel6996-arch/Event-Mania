from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class EventForm(FlaskForm):
    name = StringField('Enter name of event')
    day = StringField('Enter day of event')
    #time = StringField('Enter time of event')
    location = StringField('Enter location with Nairobi')
    owner = StringField('Enter name of event owner/ticketing manager')
    price = StringField('Enter you charges')
    submit = SubmitField('Submit') 