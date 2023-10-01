from flask import request
from flask_restful import Resource
from ..modelos import Candidato,CandidatoSchema,db
from flask_jwt_extended import current_user, jwt_required

from MicroservicioPermisos import modelos


from datetime import datetime
candidato_schema = CandidatoSchema()


class VistaCandidatos (Resource):
   
    @jwt_required()
    def get(self):
        
        if(current_user['activo'] == False):
            return 'El usuario no se encuentra activo'
        
        opcion = db.session.query(modelos.Opciones).filter_by( nombre ='verCandidatos').first()
        if(opcion == None):
            return 'No tiene permiso'
        permiso = db.session.query(modelos.Permiso).filter_by( usuarioId = current_user['id'], opcionId=opcion.id).first()

        if(permiso == None or current_user['admin']  ==False):
            return 'No tiene el permiso para consultar los candidatos'
        
        return candidato_schema.dump(db.session.query(Candidato).all())
    
    @jwt_required()
    def post(self):
        
        if(current_user['activo'] == False):
            return 'El usuario no se encuentra activo'
        
        opcion = db.session.query(modelos.Opciones).filter_by( nombre ='crearCandidato').first()
        if(opcion == None):
            return 'No tiene permiso'
        permiso = db.session.query(modelos.Permiso).filter_by( usuarioId = current_user['id'], opcionId=opcion.id).first()

        if(permiso == None or current_user['admin']  ==False):
            return 'No tiene el permiso para crear candidatos'
        
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
    