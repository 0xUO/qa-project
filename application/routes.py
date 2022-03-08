from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import User, Question
from application.forms import CreateUser, AskQuestion

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = CreateUser()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        new_user = User(username = username, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users'))
    return render_template('register.html', form = form)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    form = AskQuestion()
    users = User.query.all()
    form.asked_by_id.choices.extend((user.id, user.username)for user in users)
    if request.method == 'POST':
        subject = form.subject.data
        ask_question = form.ask_question.data
        email = form.email.data
        id = form.asked_by_id.data
        new_question = Question(subject = subject, ask_question = ask_question, email = email, answered = False, asked_by_id = id)
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('questions'))
    return render_template('ask.html', form = form)

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    quest = Question.query.all()
    return render_template('questions.html', qs = quest)

@app.route('/users', methods=['GET', 'POST'])
def users():
    list_users = User.query.all()
    return render_template('users.html', lst = list_users)

@app.route('/update/<int:q_id>')
def update(q_id):
    question = Question.query.get(q_id)
    question.answered = not question.answered
    db.session.commit()
    return redirect(url_for('questions'))

@app.route('/delete/<int:q_id>')
def delete(q_id):
    question = Question.query.get(q_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('questions'))
