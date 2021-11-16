from flask import render_template,url_for
from app import app

@app.route('/')
def events():

    return render_template('events.html')


