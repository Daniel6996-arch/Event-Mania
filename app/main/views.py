from flask import render_template,request,redirect,url_for,abort
from . import main
import urllib.request,json
import requests
from ..models import Event
from .forms import EventForm
from .. import db



@main.route('/events',methods=['GET','POST'])    
def events():
    event_form = EventForm()
    if event_form.validate_on_submit():
        new_event = Event(name = event_form.name.data, day = event_form.day.data, location = event_form.location.data,price = event_form.price.data, owner = event_form.owner.data )
        db.session.add(new_event)
        db.session.commit()
        

    return render_template('events.html', event_form = event_form)

@main.route('/newly-posted',methods=['GET','POST'])    
def recent():
    
    try:
        events = Event.query.all()
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

    return render_template('recent.html', events = events)
