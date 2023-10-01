from MicroservicioCandidato import create_app

from MicroservicioUsuario import modelos

from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .modelos import db 

from .vistas import VistaCandidato,VistaCandidatos

app = create_app('default')  
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)


api = Api(app)
api.add_resource(VistaCandidatos, "/candidatos")
api.add_resource(VistaCandidato, "/candidato/<int:id_candidato>")

jwt =JWTManager(app)


@jwt.user_lookup_loader
def _user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    user = db.session.query(modelos.Usuario).filter_by(id=identity).one_or_none()
    print('user')
    print(user.id)
    if user is not None:
        return {
            "id": user.id,
            "admin": user.admin,
            "activo": user.activo
        }
    return None

    

