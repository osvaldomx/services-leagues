from datetime import datetime

from marshmallow import Schema
from marshmallow import fields

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from . import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contrasena = db.Column(db.String(256), nullable=False)
    nacimiento = db.Column(db.Date)
    email = db.Column(db.String(50), nullable=False, unique=True)
    genero = db.Column(db.String(10))
    confirmado = db.Column(db.Boolean, default=True)
    creado = db.Column(db.DateTime, default=datetime.now())

    liga = db.relationship('Liga')
    pago = db.relationship('Pago')
    sesion = db.relationship('Sesion')

    def __init__(self, nombre, contrasena,
                    nacimiento, email, genero, confirmado):
        self.nombre = nombre
        self.contrasena = self.__generate_pass(contrasena)
        self.nacimiento = nacimiento
        self.email = email
        self.genero = genero
        self.confirmado = confirmado

    def __repr__(self):
        return "<Usuario {}>".format(self.email)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def __generate_pass(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.contrasena, password)

    @classmethod
    def authenticate(cls, email, password):
        user = cls.get_user_by_email(email)
    
        if user and cls.verify_password(user, password):
            return user    

    @staticmethod
    def get_user_by_email(value):
        return Usuario.query.filter_by(email=value).first()
    

class UsuarioSchema(Schema):
    id = fields.Int()
    nombre = fields.Str()
    contrasena = fields.Str()
    nacimiento = fields.Date()
    email = fields.Email()
    genero = fields.Str()
    confirmado = fields.Boolean()
    creado = fields.DateTime()