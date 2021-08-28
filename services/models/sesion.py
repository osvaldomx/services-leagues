from datetime import datetime

from marshmallow import Schema
from marshmallow import fields

from . import db

class Sesion(db.Model):
    __tablename__ = 'sesion'

    id = db.Column(db.Integer, primary_key=True)
    usuario_email = db.Column(db.String(50),
                                db.ForeignKey('usuario.email'))
    genero = db.Column(db.String(10))
    creada = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Sesion {}>".format(self.usuario_email)

    def __init__(self, email, genero):
        self.usuario_email = email
        self.genero = genero

    def save(self):
        db.session.add(self)
        db.session.commit()

class SesionSchema(Schema):
    id = fields.Int()
    usuario_email = fields.Str()
    genero = fields.Str()
    creado = fields.DateTime()