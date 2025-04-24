from flask import Blueprint, jsonify
from models.client import Client

client = Blueprint('client', __name__)


@client.route('/api/client')
def get_client():
    clients = Client.query.all()
    return jsonify([client.serialize() for client in clients])
import json


# Cargar datos desde el archivo JSON
def cargar_clientes():
    with open('clientes.json', 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    clientes = cargar_clientes()
    return jsonify(clientes)

