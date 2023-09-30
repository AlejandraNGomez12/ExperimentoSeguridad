import hashlib
from flask import jsonify, request
from flask_restful import Resource

from modelos import Empresa, db
from .VistaBase import empresa_schema


class VistaEmpresa(Resource):

    def get(self, id_empresa):
        return empresa_schema.dump(Empresa.query.get_or_404(id_empresa))

    def get(self):
        return [empresa_schema.dump(empresa) for empresa in empresas]

    def post(self):
        nueva_empresa = Empresa(
            nombre=request.json["nombre"],
            actividad=request.json["actividad"],
            numEmpleados=request.json["numEmpleados"]
        )

        db.session.add(nueva_empresa)
        db.session.commit()
        return empresa_schema.dump(nueva_empresa)
    
    def put(self, id_empresa):
        empresa = Empresa.query.get_or_404(id_empresa)
        empresa.nombre = request.json["nombre"]
        empresa.actividad = request.json["actividad"]
        empresa.numEmpleados = request.json["numEmpleados"]

        db.session.commit()
        return empresa_schema.dump(empresa)



