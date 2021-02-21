import datetime
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from app.extensions.db import db
# from app.models import User

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
# user_manager = UserManager(app, db, User)
# login_manager = LoginManager()
# login_manager.login_view = 'home.login'
# login_manager.init_app(app)
# QRcode(app, mode="google")

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)
#
# @login_manager.unauthorized_handler
# def handle_needs_login():
#     return redirect(url_for('home.login', msg="You have to be logged in to access this page."))

@app.context_processor
def inject_today_date():
    return {'current_date': datetime.date.today()}