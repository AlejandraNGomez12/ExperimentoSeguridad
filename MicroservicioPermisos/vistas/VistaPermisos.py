import hashlib
from flask import jsonify, request
from flask_restful import Resource
import requests

from ..modelos import Permiso,PermisoSchema,Opciones,db
from MicroservicioUsuario import modelos
from flask_jwt_extended import current_user, jwt_required
from datetime import datetime

permiso_schema = PermisoSchema()

class VistaPermisos(Resource):

    @jwt_required()
    def get(self):
        return permiso_schema.dump(db.session.query(Permiso).all())

    @jwt_required()
    def post(self):
        
        if(current_user['admin'] == False):
            return 'No tiene el permiso para crear un permiso'
        
        if(request.json["usuarioId"]== None):
            return "error"
        
        if(request.json["opcionId"]== None):
            return "error"
        print(request.json["opcionId"])
        print(request.json["usuarioId"])
        usuario = db.session.query(modelos.Usuario).filter_by(id = request.json["usuarioId"]).first()
        opcion = db.session.query(Opciones).filter_by(id = request.json["opcionId"]).first()

        if( usuario == None):
            return "no existe el id de usuario"
        if( opcion == None):
            return "no existe el id de opcion"
        
        nueva_permiso = Permiso(
            usuarioId = usuario.id,
            opcionId = opcion.id,
            usuarioCreacion = current_user["id"],
            fechaCreacion =  datetime.now()
        )

        db.session.add(nueva_permiso)
        db.session.commit()
        return permiso_schema.dump(nueva_permiso)
    