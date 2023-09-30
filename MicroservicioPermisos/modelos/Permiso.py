from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from .Permiso import db

class Opciones(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key=True)
    nombre = db.Column(db.String(50))    

class Permiso(db.Model):
    usuarioId = db.relationship(
        "Usuario", cascade="all, delete, delete-orphan"
    )
    opcionId = db.relationship(
        "Opciones", cascade="all, delete, delete-orphan"
    )
    usuarioCreacion = db.Column(db.number)
    fechaCreacion = db.Column(db.DateTime)
    

class PermisoSchema(SQLAlchemySchema):
    class Meta:
        model = Permiso
        include_relationships = True
        include_fk = True
        load_instance = True

    usuarioId = fields.String()
    opcionId = fields.String()
    usuarioCreacion = fields.Number
    fechaCreacion = fields.DateTime
   