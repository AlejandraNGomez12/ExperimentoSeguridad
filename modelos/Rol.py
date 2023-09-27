from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

from .RolPermisos import RolPermisosSchema
from .Base import db


class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    tipo = db.Column(db.String)
    permisos = db.relationship(
        "RolPermisos", cascade="all, delete, delete-orphan"
    )
    

class RolSchema(SQLAlchemySchema):
    class Meta:
        model = Rol
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.String()
    nombre = fields.String()
    tipo = fields.String()
