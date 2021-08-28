from datetime import datetime

from marshmallow import Schema
from marshmallow import fields

from . import db

class Club(db.Model):
    __tablename__ = 'club'
    
    id = db.Column(db.Integer, primary_key=True)
    estadio_id = db.Column(db.Integer,
                            db.ForeignKey('estadio.id'))
    nombre = db.Column(db.Text, unique=True, nullable=False)
    nombre_corto = db.Column(db.Text)
    ciudad = db.Column(db.String(50))
    pais = db.Column(db.String(50))
    direccion = db.Column(db.Text)
    web = db.Column(db.String(50))
    fundacion = db.Column(db.DateTime)
    logo = db.Column(db.Text)
    facebook = db.Column(db.String(100))
    creacion = db.Column(db.DateTime, default=datetime.now())

    contrato_jugador = db.relationship("ContratoJugador")
    contrato_staff = db.relationship("ContratoStaff")
    partido = db.relationship('Partido', primaryjoin="Club.id==Partido.club_local")

    def __init__(self, estadio_id, nombre, nombre_corto='',
                    ciudad='', pais='', direccion='',
                    web='', fundacion='', logo='',
                    facebook=''):
        self.estadio_id = estadio_id
        self.nombre = nombre
        self.nombre_corto = nombre_corto
        self.ciudad = ciudad
        self.pais = pais
        self.direccion = direccion
        self.web = web
        self.fundacion = fundacion
        self.logo = logo
        self.facebook = facebook

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

class ClubSchema(Schema):
    id = fields.Int()
    estado_id = fields.Int()
    nombre = fields.Str()
    nombre_corto = fields.Str()
    ciudad = fields.Str()
    pais = fields.Str()
    direccion = fields.Str()
    web = fields.Str()
    fundacion = fields.DateTime()
    logo = fields.Str()
    facebook = fields.Str()