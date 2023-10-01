from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Permiso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuarioId = db.Column(db.String)
    opcionId = db.Column(db.Integer, db.ForeignKey("opciones.id"))
    usuarioCreacion = db.Column(db.String)
    fechaCreacion = db.Column(db.DateTime)
    

class PermisoSchema(SQLAlchemySchema):
    class Meta:
        model = Permiso
        include_relationships = True
        include_fk = True
        load_instance = True

    id  = fields.String()
    usuarioId = fields.String()
    opcionId = fields.String()
    usuarioCreacion = fields.String()
    fechaCreacion = fields.DateTime()
   