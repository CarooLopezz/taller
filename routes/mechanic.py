from flask import Blueprint, request, jsonify
from models.mechanic import Mechanic
from models.db import db

mechanic = Blueprint('mechanic', __name__, url_prefix='/mechanics')

# GET all mechanics
@mechanic.route('/', methods=['GET'])
def get_all_mechanics():
    mechanics = Mechanic.query.all()
    return jsonify([m.to_json() for m in mechanics])

# GET mechanic by ID
@mechanic.route('/<int:id>', methods=['GET'])
def get_mechanic(id):
    m = Mechanic.query.get(id)
    if not m:
        return jsonify({'error': 'Mecánico no encontrado'}), 404
    return jsonify(m.to_json())

# POST create new mechanic
@mechanic.route('/', methods=['POST'])
def create_mechanic():
    data = request.get_json()
    new_mechanic = Mechanic(
        name=data['name'],
        specialty=data.get('specialty'),
        experience_years=data.get('experience_years')
    )
    db.session.add(new_mechanic)
    db.session.commit()
    return jsonify(new_mechanic.to_json()), 201

# PUT update mechanic
@mechanic.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    m = Mechanic.query.get(id)
    if not m:
        return jsonify({'error': 'Mecánico no encontrado'}), 404

    data = request.get_json()
    m.name = data.get('name', m.name)
    m.specialty = data.get('specialty', m.specialty)
    m.experience_years = data.get('experience_years', m.experience_years)

    db.session.commit()
    return jsonify(m.to_json())

# DELETE mechanic
@mechanic.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    m = Mechanic.query.get(id)
    if not m:
        return jsonify({'error': 'Mecánico no encontrado'}), 404

    db.session.delete(m)
    db.session.commit()
    return jsonify({'message': 'Mecánico eliminado'})
