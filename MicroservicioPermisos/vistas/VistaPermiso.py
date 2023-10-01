import hashlib
from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from ..modelos import Permiso,PermisoSchema,db
from datetime import datetime

permiso_schema = PermisoSchema()

class VistaPermiso(Resource):

    @jwt_required()
    def get(self, id_permiso):
        return permiso_schema.dump(Permiso.query.get_or_404(id_permiso))

    
    @jwt_required()
    def put(self, id_permiso):
        
        if(current_user['admin'] == False):
            return 'No tiene el permiso para editar un permiso'

  
        empresa = Permiso.query.get_or_404(id_permiso)
        empresa.nit = request.json["nit"]
        empresa.nombre = request.json["nombre"]
        empresa.usuarioCreacion = current_user["id"],
        empresa.fechaCreacion =  datetime.now()

        db.session.commit()
        return permiso_schema.dump(empresa)


