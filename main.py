from flask import Flask, request, jsonify
from models import db, Department
from schemas import DepartmentSchema
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)

# Ruta para agregar un nuevo departamento
@app.route('/departments', methods=['POST'])
def add_department():
    id = request.json['department_id']
    name = request.json['department_name']
    location = request.json['location']
    abrev = request.json['department_abrev']
    manager = request.json['manager_id']
    lupdate = request.json['last_updated']
    new_department = Department(department_id=id, department_name=name, department_abrev=abrev,manager_id=manager, last_updated=lupdate, location=location)
    db.session.add(new_department)
    db.session.commit()
    return department_schema.jsonify(new_department), 201

# Ruta para obtener todos los departamentos
@app.route('/departments', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    return departments_schema.jsonify(departments)

# Ruta para obtener un departamento por id
@app.route('/department/<int:id>', methods=['GET'])
def get_department(id):
    department = Department.query.get_or_404(id)
    return department_schema.jsonify(department)

# Ruta para actualizar un departamento
@app.route('/department/<int:id>', methods=['PUT'])
def update_department(id):
    department = Department.query.get_or_404(id)
    department.department_name = request.json['department_name']
    department.location = request.json['location']
    department.department_abrev = request.json['department_abrev']
    department.manager_id = request.json['manager_id']
    department.last_updated = request.json['last_updated']
    db.session.commit()
    return department_schema.jsonify(department)

# Ruta para eliminar un departamento
@app.route('/department/<int:id>', methods=['DELETE'])
def delete_department(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
