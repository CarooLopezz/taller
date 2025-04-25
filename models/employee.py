from models.db import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)

    def __init__(self, name, role, email, phone=None):
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'phone': self.phone
        }
