from app import app
from .home import home

app.register_blueprint(home)