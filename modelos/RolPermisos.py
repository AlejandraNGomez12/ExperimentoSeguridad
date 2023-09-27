from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from .Base import db


class RolPermisos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rol_id = db.Column(db.Integer, db.ForeignKey("rol.id"))
    permiso_id = db.Column(db.Integer, db.ForeignKey("permiso.id"))


class RolPermisosSchema(SQLAlchemySchema):
    class Meta:
        model = RolPermisos
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.String()
