from flask import request
from flask_restful import Resource
from modelos import Candidato,CandidatoSchema,db
from flask_jwt_extended import current_user, jwt_required

from datetime import datetime
candidato_schema = CandidatoSchema()


class VistaCandidatos (Resource):
   
    @jwt_required()
    def get(self):
        return candidato_schema.dump(db.session.query(Candidato).all())
    
    @jwt_required()
    def post(self):
        nueva_candidato = Candidato(
            usuarioCreacion = current_user["id"],
            fechaCreacion =  datetime.now(),
            documento = request.json["documento"],
            nombre = request.json["nombre"],
            fechaNacimiento = datetime.strptime(request.json["fechaNacimiento"], "%Y-%m-%d")
        )

        db.session.add(nueva_candidato)
        db.session.commit()
        return candidato_schema.dump(nueva_candidato)
    