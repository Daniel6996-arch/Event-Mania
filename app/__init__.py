from flask import Flask

# Initializing application
app = Flask(__name__, static_url_path='/static')

from app.main import views