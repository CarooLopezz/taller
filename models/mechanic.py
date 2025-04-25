from models.db import db

class Mechanic(db.Model):
    __tablename__ = 'mechanics'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=True)
    experience_years = db.Column(db.Integer, nullable=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialty': self.specialty,
            'experience_years': self.experience_years
        }
