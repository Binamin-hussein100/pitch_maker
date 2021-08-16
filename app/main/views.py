from flask import Flask,render_template
from . import main


@main.route('/')
def index():
    return render_template('home.html')
