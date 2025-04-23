 #en caso no exitir la tala modelo crearla
    
    #models routes cliente servidor
    #vista,controlador
from models.db import db #type: ignore


class Client(db.model):

    __tablename__='client' #creo la tabla cliente
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=True)
    email=db.Column(db.String, nullable=True, unique=True)
    phone=db.Column(db.String, nullnable=True)

    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone

    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'phone':self.phone,
        }