from flask_wtf import FlaskForm #creating form classes in Flask -saulceja
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class RegisterUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    confirm_registration = SubmitField('Sign-Up')

class LoginUseForm(FlaskForm):
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberLogin = BooleanField('Remember Login')
    confirm_registration = SubmitField('Submit')