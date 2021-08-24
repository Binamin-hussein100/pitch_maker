from flask import render_template,redirect,url_for,flash,request
from werkzeug.security import check_password_hash,generate_password_hash
from . import auth
from flask_login import login_user,logout_user,login_required,current_user
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db


@auth.route('/sign_up', methods = ['GET','POST'])
def register_user():
    form = RegistrationForm()
    
    
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user =  User(fname = form.first_name.data, lname = form.last_name.data, email = form.email.data,password_secure = hashed_password, username = form.username.data)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    return render_template('auth-temp/register.html',form = form)



@auth.route('/login', methods = ['GET','POST'])

def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user =  User.query.filter_by(email = login_form.email.data).first()
        
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.pitch'))
    flash("Invalid username or password!")
    return render_template('auth-temp/login.html', login_form = login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))
