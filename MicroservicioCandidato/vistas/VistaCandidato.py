from flask import request
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource
from ..modelos import Candidato,db,CandidatoSchema
from MicroservicioPermisos import modelos

candidato_schema = CandidatoSchema()


class VistaCandidato(Resource):
    
    @jwt_required()
    def get(self, id_candidato):
        
        if(current_user['activo'] == False):
            return 'El usuario no se encuentra activo'
        
        opcion = db.session.query(modelos.Opciones).filter_by( nombre ='verCandidato').first()
        if(opcion == None):
            return 'No tiene permiso'
        permiso = db.session.query(modelos.Permiso).filter_by( usuarioId = current_user['id'], opcionId=opcion.id).first()

        if(permiso == None or current_user['admin']  ==False):
            return 'No tiene el permiso para consultar el candidato'
        
        return candidato_schema.dump(Candidato.query.get_or_404(id_candidato))
        
    @jwt_required()
    def put(self, id_candidato):
        
        if(current_user['activo'] == False):
            return 'El usuario no se encuentra activo'
        
        opcion = db.session.query(modelos.Opciones).filter_by( nombre ='editarCandidato').first()
        if(opcion == None):
            return 'No tiene permiso'
        permiso = db.session.query(modelos.Permiso).filter_by( usuarioId = current_user['id'], opcionId=opcion.id).first()

        if(permiso == None or current_user['admin']  ==False):
            return 'No tiene el permiso para editar el candidato'
        
        candidato = Candidato.query.get_or_404(id_candidato)
        candidato.documento=request.json["documento"]
        candidato.nombre=request.json["nombre"]
        candidato.fechaNacimiento=request.json["fechaNacimiento"]

        db.session.commit()
        return candidato_schema.dump(candidato)
        


