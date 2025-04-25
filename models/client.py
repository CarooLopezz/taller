from models.db import db  # Asegúrate de que esta importación sea correcta

class Client(db.Model):
    __tablename__ = 'client'  # Define el nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True, unique=True)
    phone = db.Column(db.String, nullable=True)  # Corregido el error de 'nullable'

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
        }
