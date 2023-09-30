from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from .Usuario import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))
    admin = db.Column(db.Boolean)
    activo = db.Column(db.Boolean)


    def dar_atributos(self):
        return {"id": self.id, "usuario": self.usuario, "admin": self.admin.value, "activo": self.activo.value}


class UsuarioSchema(SQLAlchemySchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

    id = fields.Integer()
    usuario = fields.String()
