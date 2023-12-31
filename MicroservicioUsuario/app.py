from MicroservicioUsuario import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .modelos import (db) 
from .vistas import VistaUsuario, VistaLogIn

app = create_app('default')  
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)


api = Api(app)
api.add_resource(VistaUsuario, "/usuario")
api.add_resource(VistaLogIn, "/login")

jwt =JWTManager(app)



