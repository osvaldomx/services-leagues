from datetime import datetime

from . import db

class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'

    id = db.Column(db.Integer, primary_key=True)
    partido_id = db.Column(db.Integer, db.ForeignKey("partido.id"))
    jugador_id = db.Column(db.Integer, db.ForeignKey("jugador.id"))
    minuto = db.Column(db.Integer)
    amarilla = db.Column(db.Integer, nullable=False, default=1)
    doble_amarilla = db.Column(db.Integer, default=0)
    roja = db.Column(db.Integer, default=0)
    creacion = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, partido_id, jugador_id, minuto, amarilla,
                    doble_amarilla, roja):
        self.partido_id = partido_id
        self.jugador_id = jugador_id
        self.minuto = minuto
        self.amarilla = amarilla
        self.doble_amarilla = doble_amarilla
        self.roja = roja