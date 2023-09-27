from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .Base import db
from .Usuario import Usuario


class Empresa(Usuario):
    id = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key=True)
    nombre = db.Column(db.String(50))
    actividad = db.Column(db.String(50))
    numEmpleados = db.Column(db.String(50))

    
class EmpresaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empresa
        include_relationships = True
        load_instance = True

    id = fields.String()
