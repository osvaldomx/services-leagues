import os
import jwt

from jwt.exceptions import ExpiredSignatureError

from .responses import bad_request

from flask import request
from flask import jsonify

from functools import wraps

from datetime import datetime
from datetime import timedelta

from services.models.usuario import Usuario

class Auth():
    @staticmethod
    def create_acces_token(user):
        try:
            payload = {
                'user_id': user.id,
                'user_email': user.email,
                'exp': datetime.utcnow() + timedelta(days=5)
            }

            return jwt.encode(
                payload,
                os.getenv("SECRET_KEY"),
                algorithm='HS256'
            ).decode("utf-8")
        except Exception as e:
            print(e)
            return ""

    @staticmethod
    def decode_token(token):
        res = {
            'data':{},
            'error': {}
        }

        try:
            payload = jwt.decode(token, os.getenv("SECRET_KEY"))
            res['data'] = payload
            return res
        except jwt.ExpiredSignatureError as ese:
            print(ese)
            res['error'] = {'message': "El Token de acceso expiró, logeate para obtener otro."}
            return res
        except jwt.InvalidTokenError as ite:
            print(ite)
            res['error'] = {
                'message': "Token invalido, intentalo de nuevo con otro Token."
            }
            return res
    @staticmethod
    def user_auth_required(func):
        """
        Auth decorator
        """
        @wraps(func)
        def decorated_auth(*args, **kwargs):
            if 'Authorization' not in request.headers:
                return bad_request({
                    'error': "No se encontró Token de acceso, por favor logeate para obtener uno."
                })

            token = request.headers.get('Authorization')
            data = Auth.decode_token(token)

            if data['error']:
                return bad_request({
                    'error': data['error']['message']
                })

            email = data['data']['user_email']
            check_user = Usuario.get_user_by_email(email)

            if not check_user:
                return bad_request({
                    'error': "No se encontró Token de acceso, por favor logeate para obtener uno."
                })

            return func(*args, **kwargs)
        return decorated_auth