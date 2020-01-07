class Battleship(#db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coordination = db.Colume(db.String(30), nullable=False)
    hit_or_miss = db.Colume(db.String(30), nullable=False)


        def __repr__(self):
            return ''.join(
    
list_of_hits=[A1, B2, C3, D4]
if '''the cordination''' in list_of_hits:
    return "You hit my battleship!"
