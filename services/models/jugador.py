from datetime import datetime

from . import db

class Jugador(db.Model):
    __tablename__ = 'jugador'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    nombre_corto = db.Column(db.String(50))
    alias = db.Column(db.String(25))
    posicion = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.String(50))
    pais = db.Column(db.String(50))
    nacimiento = db.Column(db.DateTime)
    foto = db.Column(db.String(100))
    facebook = db.Column(db.String(100))
    creacion = db.Column(db.DateTime, default=datetime.now())

    contrato_jugador = db.relationship("ContratoJugador")
    alineacion = db.relationship('Alineacion')
    gol = db.relationship('Gol')
    tarjeta = db.relationship('Tarjeta')
    cambio = db.relationship('Cambio', primaryjoin="Jugador.id==Cambio.jugador_entra")

    def __init__(self, nombre, nombre_corto='',
                    posicion='', estado='', pais='',
                    nacimiento='', foto='',
                    facebook=''):
        self.nombre = nombre
        self.nombre_corto = nombre_corto
        self.posicion = posicion
        self.estado = estado
        self.pais = pais
        self.nacimiento = nacimiento
        self.foto = foto
        self.facebook = facebook
