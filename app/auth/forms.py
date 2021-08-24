from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo,ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    
    first_name = StringField('ENTER YOUR FIRST NAME: ', validators=[Required()])
    last_name = StringField('ENTER YOUR LAST NAME: ', validators=[Required()])
    username = StringField('ENTER YOUR USER NAME: ', validators=[Required()])
    email = StringField('Your email address: ', validators=[Required(),Email()])
    password = PasswordField('Password: ',validators=[Required(),EqualTo( 'password_confirm', message='Password must match')])
    password_confirm = PasswordField('Confirm password:', validators=[Required()])
    submit = SubmitField('SIGN UP')
    
    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email.')

        def validate_username(self,data_field):
            if User.query.filter_by(username = data_field.data).first():
                raise ValidationError()
            
            
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit:')