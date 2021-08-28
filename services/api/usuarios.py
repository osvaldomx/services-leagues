from flask import Blueprint
from flask import request
from flask import make_response
from flask import jsonify

from services.utils.responses import response
from services.utils.responses import bad_request
from services.utils.responses import unauthorized
from services.utils.auth import Auth

from services.models.usuario import Usuario
from services.models.usuario import UsuarioSchema
from services.models.sesion import Sesion

usuario = Blueprint('usuario', __name__)

@usuario.route("/signup", methods=['POST'])
def signup_user():
    data = request.get_json(force=True)
    
    usuario = Usuario(
        nombre=data['name'],
        contrasena=data['pass'],
        nacimiento=data['birth'],
        email=data['email'],
        genero=data['gender'],
        confirmado=True
    )

    if usuario.save():
        return response(UsuarioSchema().dump(usuario))

    return bad_request()

@usuario.route("/login", methods=['POST'])
async def login():
    data = request.get_json(force=True)
    user = Usuario.authenticate(data['email'], data['password'])

    if user:
        access_token = Auth.create_acces_token(user)

        try:
            sesion = Sesion(user.email, user.genero)
            sesion.save()
        except Exception as e:
            print(e)
            return bad_request({'error': "Datos inválidos."})

        return response({
            'access_token': access_token,
            'token_type': 'Bearer'
        })
    else:
        res = make_response(unauthorized())
        res.headers['WWW-Authenticate'] = 'Bearer'
        return res

@usuario.route("/all")
@Auth.user_auth_required
def get_all_users():
    usuarios_obj = Usuario.query.all()

    if usuarios_obj:
        return response(UsuarioSchema(many=True)
                        .dump(usuarios_obj))

    return bad_request()