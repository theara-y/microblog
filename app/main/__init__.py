from flask import Blueprint

bp = Blueprint('main', __name__)

if True:
    from app.main import routes
