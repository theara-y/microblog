from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

if True:
    from app import routes
