from flask import request
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource
from modelos import Candidato,db,CandidatoSchema

candidato_schema = CandidatoSchema()


class VistaCandidato(Resource):
    
    @jwt_required()
    def get(self, id_candidato):
        return candidato_schema.dump(Candidato.query.get_or_404(id_candidato))

    @jwt_required()
    def put(self, id_candidato):
        candidato = Candidato.query.get_or_404(id_candidato)
        candidato.documento=request.json["documento"]
        candidato.nombre=request.json["nombre"]
        candidato.fechaNacimiento=request.json["fechaNacimiento"]

        db.session.commit()
        return candidato_schema.dump(candidato)



