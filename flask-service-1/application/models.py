from application import db



class coordinates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    previous_coordinates = db.Column(db.String(10), nullable=False)  #, unique=True, primary_key=True)

    def __repr__(self):
        return ''.join([
            'Coordinates: ', self.coordinates
        ])

#the application generates the random coordinates and passes it to SQL for storage. The SQL will then keep track of what coordiantes have already been through. The game will end when the ship has been sunk or all the possible coordinates have been exhausted. 



