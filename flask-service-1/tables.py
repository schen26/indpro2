from flask_services import db

class Battleship(#db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response = db.Colume(db.String(30), nullable=False)


        def __repr__(self):
            return ''.join([

class coordination(#db.Model):
    id = db.Column(db.Integer, primary_key=True)
    random_alphabet = db.Colume(db.String(30), nullable=False)
    random_number = db.Column(db.Integer, nullable=False)
