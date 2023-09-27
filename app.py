from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from modelos import (
    Admin,
    Candidato,
    Rol,
    Usuario,
    Empresa,
    db,
    Permiso,
    RolPermisos,
    
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dbapp.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "frase-secreta"
app.config["PROPAGATE_EXCEPTIONS"] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)



