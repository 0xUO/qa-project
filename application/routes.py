from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import User, Question
from application.forms import AskQuestion, CreateUser

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = CreateUser()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        new_user = CreateUser(username = username, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.html'))
    return render_template('register.html', form = form)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    form = AskQuestion()
    if request.method == 'POST':
        username = form.username.data
        subject = form.subject.data
        ask_question = form.ask_question.data
        new_question = Question(username = username, subject = subject, ask_question = ask_question)
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('questions.html'))
    return render_template('ask.html', form = form)

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    questions = '<br>'.join(str(i) for i in Question.query.all())
    return render_template('questions.html', questions=questions)

@app.route('/users', methods=['GET', 'POST'])
def users():
    list_users = '<br>'.join(str(i) for i in User.query.all())
    return render_template('users.html', list_users = list_users)