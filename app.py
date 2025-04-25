from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.client import client
from routes.product import product
from routes.service import service  
from routes.employee import employee
from routes.mechanic import mechanic  # Importamos las rutas de mechanic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(client)
app.register_blueprint(product)
app.register_blueprint(service) 
app.register_blueprint(employee)
app.register_blueprint(mechanic)  # Registramos las rutas del mecánico

@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

# Crear tablas automáticamente
from models.client import Client
from models.products import Products
from models.service import Service
from models.employee import Employee
from models.mechanic import Mechanic  # Asegúrate de que el modelo de mecánico esté importado

with app.app_context():
    db.create_all()  # Esto crea las tablas en la base de datos

if __name__ == '__main__':
    app.run(debug=True)
