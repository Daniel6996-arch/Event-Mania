from flask import render_template,redirect,url_for,flash,request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def events():

    return '<h1>Event works</h1>'


if __name__ == '__main__':
    app.run(debug = True)