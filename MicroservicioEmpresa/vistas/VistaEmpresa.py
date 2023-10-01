from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from modelos import Empresa,EmpresaSchema,db
from datetime import datetime

empresa_schema = EmpresaSchema()

class VistaEmpresa(Resource):

    def get(self, id_empresa):
       return empresa_schema.dump(Empresa.query.get_or_404(id_empresa))

    
    def put(self, id_empresa):
        empresa = Empresa.query.get_or_404(id_empresa)
        empresa.nit = request.json["nit"]
        empresa.nombre = request.json["nombre"]

        db.session.commit()
        return empresa_schema.dump(empresa)


