from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Opciones(db.Model):
    __tablename__ = "opciones"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class OpcionesSchema(SQLAlchemySchema):
    class Meta:
        model = Opciones
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.String()
    nombre = fields.String()