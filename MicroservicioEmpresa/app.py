from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from modelos import (
    Empresa,
    db   
)

from vistas.VistaEmpresa import VistaEmpresa
from vistas.VistaEmpresas import VistaEmpresas


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\aleja\\Documents\\Maestria\\ArquitecturaAgil\\ProyectoSeguridad\\ExperimentoSeguridad\\instance\\dbapp.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "frase-secreta"
app.config["PROPAGATE_EXCEPTIONS"] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)


api = Api(app)
api.add_resource(VistaEmpresas, "/empresas")
api.add_resource(VistaEmpresa, "/empresa/<int:id_empresa>")



