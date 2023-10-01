from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuarioCreacion = db.Column(db.Numeric)
    fechaCreacion = db.Column(db.DateTime)
    documento = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    fechaNacimiento = db.Column(db.Date)
    
    def dar_atributos(self):
        return {"id": self.id, "usuarioCreacion": self.usuarioCreacion, "fechaCreacion": self.fechaCreacion, "documento": self.documento, "nombre":self.nombre, "fechaNacimiento":self.fechaNacimiento}


class CandidatoSchema(SQLAlchemySchema):
    class Meta:
        model = Candidato
        include_relationships = True
        load_instance = True

    id = fields.Integer()
    usuarioCreacion = fields.Number()
    fechaCreacion = fields.DateTime()
    documento = fields.String()
    nombre = fields.String()
    fechaNacimiento = fields.Date()

