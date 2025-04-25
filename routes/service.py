from flask import Blueprint, request, jsonify
from models.service import Service
from models.db import db

service = Blueprint('service', __name__)

@service.route('/api/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([s.serialize() for s in services])

@service.route('/api/add_service', methods=['POST'])
def add_service():
    data = request.get_json()
    if not data or not all(k in data for k in ['name', 'price']):
        return jsonify({'error': 'Faltan datos'}), 400

    new_service = Service(data['name'], data['price'], data.get('description'))
    db.session.add(new_service)
    db.session.commit()

    return jsonify({'message': 'Servicio agregado', 'service': new_service.serialize()}), 201
