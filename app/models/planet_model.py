from app import db

# Create the class that is inherited from the db.Model from SQLAlchemy
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    rings = db.Column(db.Integer)
    moon_id = db.Column(db.Integer, db.ForeignKey('moon.id'))
    moon = db.relationship("Moon", back_populates="Planet")
    
    
    
# class Dog(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String)
#     breed = db.Column(db.String)
#     age = db.Column(db.Integer)
#     gender = db.Column(db.String, default="non-binary")
#     caretaker_id = db.Column(db.Integer, db.ForeignKey('caretaker.id'))
#     caretaker = db.relationship("Caretaker", back_populates="dogs")
