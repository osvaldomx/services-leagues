from datetime import datetime

from . import db

class Arbitro(db.Model):
    __tablename__ = 'arbitro'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    puesto = db.Column(db.String(50))
    pais = db.Column(db.String(50))
    creacion = db.Column(db.DateTime, default=datetime.now())

    partido = db.relationship('Partido', primaryjoin="Arbitro.id==Partido.arbitro_central")

    def __init__(self, nombre, puesto, pais):
        self.nombre = nombre
        self.puesto = puesto
        self.pais = pais