import hashlib
from flask import jsonify, request
from flask_restful import Resource

from modelos import Opciones,OpcionesSchema,db
from datetime import datetime

opciones_schema = OpcionesSchema()

class VistaOpcion(Resource):

    def get(self, id_opcion):
        return opciones_schema.dump(Opciones.query.get_or_404(id_opcion))

    
    def put(self, id_opcion):
        empresa = Opciones.query.get_or_404(id_opcion)
        empresa.nombre = request.json["nombre"]

        db.session.commit()
        return opciones_schema.dump(empresa)


