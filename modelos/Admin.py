from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .Rol import Rol
from .Base import db
from .Usuario import Usuario


class Admin(Usuario):
    id = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key=True)
    nombre = db.Column(db.String(50))

    
class AdminSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Admin
        include_relationships = True
        load_instance = True

    id = fields.String()
