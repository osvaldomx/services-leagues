from datetime import datetime

from . import db

class Temporada(db.Model):
    __tablename__ = 'temporada'

    id = db.Column(db.Integer, primary_key=True)
    liga_id = db.Column(db.Integer, db.ForeignKey('liga.id'))
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(500))
    activa = db.Column(db.Integer, default=0)
    creacion = db.Column(db.DateTime, default=datetime.now())

    contrato_jugador = db.relationship("ContratoJugador")
    contrato_staff = db.relationship("ContratoStaff")
    fase = db.relationship('Fase')
    partido = db.relationship('Partido')

    def __init__(self, nombre, descripcion, liga_id):
        self.nombre = nombre
        self.descripcion = descripcion
        self.liga_id = liga_id