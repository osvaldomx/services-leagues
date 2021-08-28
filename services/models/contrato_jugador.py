from datetime import datetime

from . import db

class ContratoJugador(db.Model):
    __tablename__ = "contrato_jugador"

    id = db.Column(db.Integer, primary_key=True)
    jugador_id = db.Column(db.Integer,
                            db.ForeignKey("jugador.id"))
    numero = db.Column(db.Integer)
    club_id = db.Column(db.Integer,
                        db.ForeignKey("club.id"))
    temporada_id = db.Column(db.Integer,
                                db.ForeignKey("temporada.id"))
    creacion = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, jugador_id, numero,
                    club_id,temporada_id):
        self.jugador_id = jugador_id
        self.numero = numero
        self.club_id = club_id
        self.temporada_id = temporada_id