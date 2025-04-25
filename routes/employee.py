from flask import Blueprint, request, jsonify
from models.employee import Employee
from models.db import db

employee = Blueprint('employee', __name__)

@employee.route('/api/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([e.serialize() for e in employees])

@employee.route('/api/add_employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    if not data or not all(k in data for k in ['name', 'role', 'email']):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    new_employee = Employee(data['name'], data['role'], data['email'], data.get('phone'))
    db.session.add(new_employee)
    db.session.commit()

    return jsonify({'message': 'Empleado agregado', 'employee': new_employee.serialize()}), 201
