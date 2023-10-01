import hashlib
from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from modelos import Empresa,EmpresaSchema,db
from datetime import datetime

empresa_schema = EmpresaSchema()

class VistaEmpresas(Resource):

    def get(self):
        return empresa_schema.dump(db.session.query(Empresa).all())

    def post(self):
        nueva_empresa = Empresa(
            nit=request.json["nit"],
            nombre=request.json["nombre"],
            usuarioCreacion = current_user["id"],##float(request.json["usuarioCreacion"]),
            fechaCreacion =  datetime.now()            
        )

        db.session.add(nueva_empresa)
        db.session.commit()
        return empresa_schema.dump(nueva_empresa)
    