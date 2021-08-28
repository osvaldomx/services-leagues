from datetime import datetime

from . import db

class Cambio(db.Model):
    __tablename__ = 'cambio'

    id = db.Column(db.Integer, primary_key=True)
    jugador_entra = db.Column(db.Integer, db.ForeignKey("jugador.id"))
    jugador_sale = db.Column(db.Integer, db.ForeignKey("jugador.id"))
    partido_id = db.Column(db.Integer, db.ForeignKey("partido.id"))
    minuto = db.Column(db.Integer)
    creacion = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, jugador_entra, jugador_sale, partido_id,
                    minuto):
        self.jugador_entra = jugador_entra
        self.jugador_sale = jugador_sale
        self.partido_id = partido_id
        self.minuto = minuto