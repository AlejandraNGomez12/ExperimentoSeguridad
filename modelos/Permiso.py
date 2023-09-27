from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema

from .Base import db


class Permiso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    accion = db.Column(db.String(128))

class PermisoSchema(SQLAlchemySchema):
    class Meta:
        model = Permiso
        load_instance = True

    id = fields.Integer()
    nombre = fields.String()
    accion = fields.String()
