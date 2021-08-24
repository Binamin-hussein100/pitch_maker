from app.models import Pitch
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Required

class pitchForm(FlaskForm):
    pitch = TextAreaField('The one-time chance.', validators=[Required()], render_kw={"placeholder": "Type a pitch..."})
    author = StringField("Your name", validators=[Required()])
    submit = SubmitField('Pitch')
    
class commentForm(FlaskForm):
    comment = StringField('', validators=[Required()])
    submit = SubmitField('Comment')