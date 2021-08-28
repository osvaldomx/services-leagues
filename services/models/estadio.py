from datetime import datetime

from marshmallow import Schema
from marshmallow import fields

from . import db

class Estadio(db.Model):
    __tablename__ = 'estadio'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(500))
    ciudad = db.Column(db.String(50))
    web = db.Column(db.String(50))
    creacion = db.Column(db.DateTime, default=datetime.now())

    club = db.relationship('Club')
    partido = db.relationship('Partido')

    def __init__(self, nombre, direccion='',
                    ciudad='', web=''):
        self.nombre = nombre
        self.direccion = direccion
        self.cuidad = ciudad
        self.web = web

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

class EstadioSchema(Schema):
    id = fields.Int()
    nombre = fields.Str()
    direccion = fields.Str()
    ciudad = fields.Str()
    web = fields.Str()
    creacion = fields.DateTime()