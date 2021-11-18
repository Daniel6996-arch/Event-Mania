from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class EventForm(FlaskForm):
    name = StringField('Enter a topic')
    time = StringField('Enter a topic')
    location = StringField('Enter a topic')
    owner = StringField('Enter a topic')
    price = StringField('Enter a topic')
    submit = SubmitField('Submit') 