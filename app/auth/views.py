from flask import render_template,redirect,url_for,flash,request
from . import auth
from flask_login import login_user,logout_user,login_required,current_user
from ..models import User
from .forms import RegistrationForm
from .. import db

@auth.route('/login', methods = ['GET','POST'])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        user =  User(firstname = form.first_name.data, lastname = form.last_name.data, username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()