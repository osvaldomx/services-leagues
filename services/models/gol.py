from datetime import datetime

from . import db

class Gol(db.Model):
    __tablename__ = 'gol'

    id = db.Column(db.Integer, primary_key=True)
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'))
    jugador_id = db.Column(db.Integer, db.ForeignKey('jugador.id'))
    minuto = db.Column(db.Integer, nullable=False)
    asistencia = db.Column(db.Integer)
    autogol = db.Column(db.Integer, default=0)
    penal = db.Column(db.Integer, default=0)
    creacion = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, partido_id, jugador_id, minuto, asistencia,
                    autogol, penal):
        self.partido_id = partido_id
        self.jugador_id = jugador_id
        self.minuto = minuto
        self.asistencia = asistencia
        self.autogol = autogol
        self.penal = penal