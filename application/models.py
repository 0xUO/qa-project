from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    questions = db.relationship('Question', foreign_keys='Question.asked_by_id', backref='user', passive_deletes=True)
    def __str__(self):   
        return f"{self.username}"

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.Text)
    ask_question = db.Column(db.Text)
    asked_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __str__(self):   
        return f"{self.asked_by_id}:\n{self.subject}:\n{self.ask_question}"

