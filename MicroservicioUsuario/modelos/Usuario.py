from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

db = SQLAlchemy()

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

class Sesion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    fechaIngreso = db.Column(db.DateTime)
    exitoso = db.Column(db.Boolean)


    def dar_atributos(self):
        return {"id": self.id, "usuario": self.usuario, "fechaIngreso": self.fechaIngreso.value, "exitoso": self.exitoso.value}


class SesionSchema(SQLAlchemySchema):
    class Meta:
        model = Sesion
        include_relationships = True
        load_instance = True

    id = fields.Integer()
    usuario = fields.String()
    fechaIngreso = fields.DateTime
    exitoso = fields.Boolean