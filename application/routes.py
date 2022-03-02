from flask import redirect, url_for, render_template, request
from sqlalchemy import desc
from application import app, db
from application.models import User, Question

@app.route('/')
def index():
    return render_template('index.html')
