from urllib import response
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Question, User

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "secret key test",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )

        return app

    def setUp(self):
        db.create_all()
        sample_user = User(username = "anon", password = "test")
        sample_question = Question(subject = "Random", ask_question = "what is 5 + 5", email = 'test@gmail.com', asked_by_id = 'anon')

        db.session.add(sample_user)
        db.session.add(sample_question)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
#-----------------------------------------------------------

class TestCreateUser(TestBase):
    def test_register_get(self):
        response = self.client.get(url_for('register'))
        self.assert200(response)
        self.assertIn(b'Usernmame', response.data)

    def test_register_post(self):
        response = self.client.post(
            url_for('register'),
            data = dict(username = 'anon', password = 'test'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'anon', response.data)

class TestUsers(TestBase):
    def test_users_get(self):
        response = self.client.get(url_for('users'))
        self.assert200(response)

class TestQuestions(TestBase):
    def test_questions_get(self):
        response = self.client.get(url_for('questions'))
        self.assert200(response)

class TestAskQuestion(TestBase):
    def test_ask_get(self):
        response = self.client.get(url_for('ask'))
        self.assert200(response)
        self.assertIn(b'Your Question: ', response.data)

    def test_ask_post(self):
        response = self.client.post(
            url_for('ask'),
            data = dict(subject = 'Random', ask_question = '1+1?', email = 'testo@gmail.com', asked_by_id = 'anon'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Random', response.data)

# python3 -m pytest

# python3 -m pytest --cov=application