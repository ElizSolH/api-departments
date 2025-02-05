from flask_marshmallow import Marshmallow
from models import Department

ma = Marshmallow()

# Esquema de serialización
class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        load_instance = True

