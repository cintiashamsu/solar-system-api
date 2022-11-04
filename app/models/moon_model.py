from app import db

# Create the class that is inherited from the db.Model from SQLAlchemy
class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)
    planet = db.relationship("Planet", back_populates="Moon")
