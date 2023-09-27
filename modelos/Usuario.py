from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from .Rol import Rol
from .Base import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))
    rol_id = db.Column(db.Integer, db.ForeignKey("rol.id"))
    
    def dar_atributos(self):
        return {"id": self.id, "usuario": self.usuario, "rol": self.rol.value}


class UsuarioSchema(SQLAlchemySchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

    id = fields.Integer()
    usuario = fields.String()
    rol = fields.Function(lambda obj: obj.rol.value)
