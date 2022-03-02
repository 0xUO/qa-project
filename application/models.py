from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    pwd = db.Column(db.String(50))
    honourable = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.Text)
    answr = db.Column(db.Text)
    asked_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    honourable_id = db.Column(db.Integer, db.ForeignKey('user.id'))