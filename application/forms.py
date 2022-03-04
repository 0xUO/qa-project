from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from datetime import date
from application.models import Question, User

class CreateUser(FlaskForm):
    username = StringField('Usernmame', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AskQuestion(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    subject = StringField('Subject')
    ask_question = StringField('Ask Question', validators=[DataRequired()])
    submit = SubmitField('Submit Question')