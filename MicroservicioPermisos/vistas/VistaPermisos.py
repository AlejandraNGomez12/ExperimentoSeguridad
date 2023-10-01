import hashlib
from flask import jsonify, request
from flask_restful import Resource
import requests

from modelos import Permiso,PermisoSchema,db
from flask_jwt_extended import current_user, jwt_required
from datetime import datetime

permiso_schema = PermisoSchema()

class VistaPermisos(Resource):

    def get(self):
        return permiso_schema.dump(db.session.query(Permiso).all())

    def post(self):
        if(int(request.json["usuarioId"])== None):
            return "error"
        
        if(int(request.json["opcionId"])== None):
            return "error"
        
        ##try:
        ##    content = requests.get('http://127.0.0.1:5001/usuario/'+int(request.json["usuarioId"]))
        ##    estado = content.status_code
            
        ##except requests.exceptions.RequestException as e:
        ##    estado = 'Error'
        
        try:
            id = (request.json["opcionId"])
            content = requests.get('http://127.0.0.1:5000/opcion/'+id)
            estado = content.status_code
            
        except requests.exceptions.RequestException as e:
            estado = 'Error'
        
        if(estado!=200):
            return 'No existe'

        nueva_permiso = Permiso(
            usuarioId = request.json["usuarioId"],
            opcionId =  request.json["opcionId"],
            usuarioCreacion = current_user["id"], ##request.json["usuarioCreacion"],
            fechaCreacion =  datetime.now()
        )

        db.session.add(nueva_permiso)
        db.session.commit()
        return permiso_schema.dump(nueva_permiso)
    