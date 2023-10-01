from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from ..modelos import Empresa,EmpresaSchema,db
from datetime import datetime
from MicroservicioPermisos import modelos

empresa_schema = EmpresaSchema()

class VistaEmpresa(Resource):

    @jwt_required()
    def get(self, id_empresa):
        opcion = db.session.query(modelos.Opciones).filter_by( nombre ='verEmpresa').first()
        if(opcion == None):
            return 'No tiene permiso'
        permiso = db.session.query(modelos.Permiso).filter_by( usuarioId = current_user['id'], opcionId=opcion.id).first()

        if(permiso == None or current_user['admin'] ==False):
            return 'No tiene el permiso para consultar la empresa'

        return empresa_schema.dump(Empresa.query.get_or_404(id_empresa))

    
    @jwt_required()
    def put(self, id_empresa):
        opcion = db.session.query(modelos.Opciones).filter_by( nombre ='editarEmpresa').first()
        if(opcion == None):
            return 'No tiene permiso'
        permiso = db.session.query(modelos.Permiso).filter_by( usuarioId = current_user['id'], opcionId=opcion.id).first()

        if(permiso == None or current_user['admin'] ==False ):
            return 'No tiene el permiso para editar la empresa'

        
        empresa = Empresa.query.get_or_404(id_empresa)
        empresa.nit = request.json["nit"]
        empresa.nombre = request.json["nombre"]

        db.session.commit()
        return empresa_schema.dump(empresa)


