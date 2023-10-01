from flask import request
from ..modelos import db, Usuario, UsuarioSchema, Sesion
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token
import hashlib
import datetime

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
        usuarioInput = Usuario.query.filter(Usuario.usuario == request.json["usuario"]).first()
        contrasena_encriptada = hashlib.md5(request.json["contrasena"].encode('utf-8')).hexdigest()
        user_sesion = request.json["usuario"]
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == contrasena_encriptada, Usuario.activo == True).first() 
        db.session.commit()         
        if usuario is None:  
            now = datetime.datetime.now()
            nueva_sesion = Sesion(usuario=user_sesion, fechaIngreso=now, exitoso = False)        
            db.session.add(nueva_sesion)
            db.session.commit()
            numero_de_sesiones_invalidas = Sesion.query.filter(Sesion.exitoso == False).count()
            mensaje = 'Usuario incorrecto.'
            if numero_de_sesiones_invalidas > 2:
                if usuarioInput:                   
                    usuarioInput.activo = False
                    db.session.commit()                  
                mensaje = 'Tiene '+ numero_de_sesiones_invalidas.usuario +' intentos invalidos. Usuario Bloqueado.'
            return mensaje, 404
        else:            
            token_de_acceso = create_access_token(identity=usuario.id) 
            now = datetime.datetime.now()
            nueva_sesion = Sesion(usuario=user_sesion, fechaIngreso=now, exitoso = True)        
            db.session.add(nueva_sesion)
            db.session.commit()                    
            return {"mensaje": "Inicio de sesión exitoso",
                "token": token_de_acceso,
                "id": usuario.id                      
            }
        
