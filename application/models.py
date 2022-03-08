from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    aksed_by_id = db.relationship('Question', backref='user', passive_deletes=True)

    def __str__(self):   
        return f"{self.id}: {self.username}"

class Question(db.Model):
    q_id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.Text)
    ask_question = db.Column(db.Text)
    email = db.Column(db.Text)
    answered = db.Column(db.Boolean)
    asked_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __str__(self):
        return f"Question ID: {self.q_id} || Username: {self.user.username} || User ID: {self.asked_by_id} || \n Subject: {self.subject} || \n Question: {self.ask_question}\
             || \n Asker Email: {self.email} ||| \n This Question been answered ?  :::  {self.answered}  ::: "