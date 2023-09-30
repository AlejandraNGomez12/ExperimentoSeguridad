from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from .Candidato import db



class Candidato():
    id = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key=True)
    usuarioCreacion = db.Column(db.number)
    fechaCreacion = db.Column(db.DateTime)
    documento = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    fechaNacimiento = db.Column(db.Date)
    
class CandidatoSchema(SQLAlchemySchema):
    class Meta:
        model = Candidato
        include_relationships = True
        load_instance = True

    id = fields.Integer()
    usuarioCreacion = fields.Number
    fechaCreacion = fields.DateTime
    documento = fields.String()
    nombre = fields.String()
    fechaNacimiento = fields.Date

