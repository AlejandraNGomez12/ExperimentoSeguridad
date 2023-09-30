from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .Empresa import db


class Empresa():
    id = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key=True)
    nit = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    usuarioCreacion = db.Column(db.number)
    fechaCreacion = db.Column(db.DateTime)
    

    
class EmpresaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empresa
        include_relationships = True
        load_instance = True

    id = fields.String()
