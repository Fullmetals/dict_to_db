from flask import Flask

app = Flask(__name__)

# Import the application views
from app import views