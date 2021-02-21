from flask import Blueprint, jsonify, request, url_for, render_template, redirect, flash

# from app.mfe_model import (us)

from app.extensions import db

home = Blueprint('home', __name__)

@home.route('/')
def route_default():
    return "Hello World"