from datetime import datetime

from . import db

class Alineacion(db.Model):
    __tablename__ = 'alineacion'

    id = db.Column(db.Integer, primary_key=True)
    partido_id = db.Column(db.Integer, db.ForeignKey("partido.id"))
    jugador_id = db.Column(db.Integer, db.ForeignKey("jugador.id"))
    titular = db.Column(db.Integer, nullable=False)
    suplente = db.Column(db.Integer, nullable=False)
    creacion = db.Column(db.DateTime, default=datetime)

    def __init__(self, partido_id, jugador_id, titular, suplente):
        self.partido_id = partido_id
        self.jugador_id = jugador_id
        self.titular = titular
        self.suplente = suplente