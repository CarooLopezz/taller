 #en caso no exitir la tala modelo crearla
    
    #models routes cliente servidor
    #vista,controlador
from models.db import db #type: ignore


class Client(db.model):

    """ __tablename__='client' #creo la tabla cliente
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=True)
    email=db.Column(db.String, nullable=True, unique=True)
    phone=db.Column(db.String, nullnable=True) """
    
    class Cliente:
        def __init__(self, nombre, direccion, celular, email):
            self.nombre = nombre
            self.direccion = direccion
            self.celular = celular
            self.email = email
            
        def mostrar_informacion(self):
            return f"Cliente: {self.nombre}, Dirección: {self.direccion}, Celular: {self.celular}, Email: {self.email}"

