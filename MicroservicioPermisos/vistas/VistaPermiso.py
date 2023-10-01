import hashlib
from flask import jsonify, request
from flask_restful import Resource

from modelos import Permiso,PermisoSchema,db
from datetime import datetime

permiso_schema = PermisoSchema()

class VistaPermiso(Resource):

    def get(self, id_permiso):
        return permiso_schema.dump(Permiso.query.get_or_404(id_permiso))

    
    def put(self, id_permiso):
        empresa = Permiso.query.get_or_404(id_permiso)
        empresa.nit = request.json["nit"]
        empresa.nombre = request.json["nombre"]

        db.session.commit()
        return permiso_schema.dump(empresa)


