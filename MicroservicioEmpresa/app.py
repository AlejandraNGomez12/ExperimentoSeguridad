from MicroservicioEmpresa import create_app

from MicroservicioUsuario import modelos

from flask_restful import Resource, Api
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .modelos import db 

from .vistas import VistaEmpresas,VistaEmpresa

app = create_app('default')  
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)


api = Api(app)
api.add_resource(VistaEmpresas, "/empresas")
api.add_resource(VistaEmpresa, "/empresa/<int:id_empresa>")

jwt =JWTManager(app)


@jwt.user_lookup_loader
def _user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    user = db.session.query(modelos.Usuario).filter_by(id=identity).one_or_none()
    if user is not None:
        if user.activo:
            return {
                "id": user.id,
                "admin": user.admin,
                "activo": user.activo
            }
        else:
            return "El usuario no se encuentra activo"
    return None

    

