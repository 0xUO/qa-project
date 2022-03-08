from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from datetime import date
from application.models import Question, User

class CreateUser(FlaskForm):
    username = StringField('Usernmame', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AskQuestion(FlaskForm):
    subject = StringField('Question Subject')
    ask_question = StringField('Your Question: ', validators=[DataRequired()])
    email = StringField('Your E-mail: ', validators=[DataRequired()])
    asked_by_id = SelectField('Link to your user: ', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit Question')