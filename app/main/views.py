
from flask_wtf import form
from ..models import Comment, Pitch, User
from app.main.forms import pitchForm,commentForm
from flask import render_template,url_for,redirect
from flask_login import login_required, current_user
from . import main
from .. import db


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home',methods=['GET', 'POST'])
def pitch():
   form = pitchForm()
   if form.validate_on_submit():
       post = Pitch(pitch = form.pitch.data, author = form.author.data) 
       db.session.add(post)
       db.session.commit()
       
       return redirect(url_for('main.pitch'))
   pitches = Pitch.query.all()
   return render_template('home_page.html',form = form, pitches = pitches) 

@main.route('/comments', methods = ['GET','POST'])
def comment():
    
    comment_form = commentForm()
    print(comment_form)
    if comment_form.validate_on_submit():
        new_comment = Comment( comments = comment_form.comment.data)
        db.session.add(new_comment)
        db.session.commit()
        # flash('Your comment has been published.')
        return redirect(url_for('main.comment'))
    comments = Comment.query.all()
    return render_template('comments.html', comment_form = comment_form, comments = comments  )
    
    