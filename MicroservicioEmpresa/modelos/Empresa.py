from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Empresa(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    nit = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    usuarioCreacion = db.Column(db.Numeric)
    fechaCreacion = db.Column(db.DateTime)
    

    
class EmpresaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empresa
        include_relationships = True
        load_instance = True

    id = fields.String()
    nit = fields.String()
    nombre = fields.String()
    usuarioCreacion = fields.Number()
    fechaCreacion = fields.DateTime()
    