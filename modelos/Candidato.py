from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from .Rol import Rol
from .Base import db
from .Usuario import Usuario


class Candidato(Usuario):
    id = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key=True)
    nombre = db.Column(db.String(50))
    

class CandidatoSchema(SQLAlchemySchema):
    class Meta:
        model = Candidato
        include_relationships = True
        load_instance = True

    id = fields.Integer()
    usuario = fields.String()
    nombre = fields.String()

