import hashlib
from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from ..modelos import Opciones,OpcionesSchema,db

opciones_schema = OpcionesSchema()

class VistaOpciones(Resource):

    @jwt_required()
    def get(self):
        return opciones_schema.dump(db.session.query(Opciones).all())

    @jwt_required()
    def post(self):
        nueva_opcion = Opciones(
            nombre=request.json["nombre"],
        )

        db.session.add(nueva_opcion)
        db.session.commit()
        return opciones_schema.dump(nueva_opcion)
    