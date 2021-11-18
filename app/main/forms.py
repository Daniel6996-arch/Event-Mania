<<<<<<< HEAD
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
=======
<<<<<<< HEAD
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField

class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
=======
from flask_wtf import FlaskForm 
from wtforms import SelectField,StringField,SubmitField,TextAreaField,PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
>>>>>>> 2c38bc68549c550e73e7b665f4eee9da4fa87299
>>>>>>> 721619b390f7e6556acb8d72426a8f5cb5b3d85d
