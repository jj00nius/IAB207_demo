from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, PasswordField, SubmitField, StringField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo

class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    # Adding two validators:
    # One to ensure input is entered
    # Other to check if the description meets the length requirements
    description = TextAreaField('Description', validators=[InputRequired()])
    image = StringField('Cover Image', validators=[InputRequired()])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField('Create')

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Create')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')