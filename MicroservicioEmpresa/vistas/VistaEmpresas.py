import hashlib
from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from ..modelos import Empresa,EmpresaSchema,db
from datetime import datetime
from MicroservicioPermisos import modelos

empresa_schema = EmpresaSchema()

class VistaEmpresas(Resource):

    @jwt_required()
    def get(self):
        opcion = db.session.query(modelos.Opciones).filter_by( nombre ='verEmpresa').first()
        if(opcion == None):
            return 'No tiene permiso'
        permiso = db.session.query(modelos.Permiso).filter_by( usuarioId = current_user['id'], opcionId=opcion.id).first()

        if(permiso == None or current_user['admin']  ==False):
            return 'No tiene el permiso para consultar las Empresas'
        
        return empresa_schema.dump(db.session.query(Empresa).all())

    @jwt_required()
    def post(self):
        opcion = db.session.query(modelos.Opciones).filter_by( nombre ='crearEmpresa').first()
        if(opcion == None):
            return 'No tiene permiso'
        permiso = db.session.query(modelos.Permiso).filter_by( usuarioId = current_user['id'], opcionId=opcion.id).first()

        if(permiso == None or current_user['admin']  ==False):
            return 'No tiene el permiso para crear una empresa'
        
        nueva_empresa = Empresa(
            nit=request.json["nit"],
            nombre=request.json["nombre"],
            usuarioCreacion = current_user["id"],
            fechaCreacion =  datetime.now()            
        )

        db.session.add(nueva_empresa)
        db.session.commit()
        return empresa_schema.dump(nueva_empresa)
    