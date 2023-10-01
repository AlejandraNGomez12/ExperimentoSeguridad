import hashlib
from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from ..modelos import Opciones,OpcionesSchema,db
from datetime import datetime

opciones_schema = OpcionesSchema()

class VistaOpcion(Resource):

    @jwt_required()
    def get(self, id_opcion):
        return opciones_schema.dump(Opciones.query.get_or_404(id_opcion))

    @jwt_required()
    def put(self, id_opcion):
        
        opcion = Opciones.query.get_or_404(id_opcion)
        opcion.nombre = request.json["nombre"]

        db.session.commit()
        return opciones_schema.dump(opcion)


