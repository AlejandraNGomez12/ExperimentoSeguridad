from flask import request
from ..modelos import db, Usuario, UsuarioSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token
import hashlib

usuario_schema = UsuarioSchema()

class VistaUsuario(Resource):    
    def post(self):        
            usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"]).first()
            if usuario is None:
                contrasena_encriptada = hashlib.md5(request.json["contrasena"].encode('utf-8')).hexdigest()
                nuevo_usuario = Usuario(usuario=request.json["usuario"], contrasena=contrasena_encriptada, admin =request.json['admin'], activo = request.json['activo']) 
                db.session.add(nuevo_usuario)
                db.session.commit()               
                return {"mensaje": "usuario creado exitosamente"}
            else:
                return "El usuario ya existe", 404
        
class VistaLogIn(Resource):
    def post(self):
        contrasena_encriptada = hashlib.md5(request.json["contrasena"].encode('utf-8')).hexdigest()
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == contrasena_encriptada).first()        
        db.session.commit()      
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            #guardar session
            return {"mensaje": "Inicio de sesión exitoso",
                "token": token_de_acceso,
                "id": usuario.id                
            }
