from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Department(db.Model):
    __tablename__ = 'Departments_2'  # El nombre de la tabla en la base de datos
    
    department_id = db.Column(db.Integer, primary_key=True, nullable=False)  # ID del departamento
    department_name = db.Column(db.String(100), nullable=False)  # Nombre del departamento
    location = db.Column(db.String(100), nullable=False)  # Ubicación del departamento
    department_abrev = db.Column(db.String(10), nullable=False)  # Abreviatura del departamento
    manager_id = db.Column(db.String(100), nullable=False)  # Manager del departamento
    last_updated = db.Column(db.DateTime, nullable=False)  # Fecha de última actualización
    
    def __init__(self, department_id, department_name, location, department_abrev, manager_id, last_updated):
        self.department_id = department_id
        self.department_name = department_name
        self.location = location
        self.department_abrev = department_abrev
        self.manager_id = manager_id
        self.last_updated = last_updated
