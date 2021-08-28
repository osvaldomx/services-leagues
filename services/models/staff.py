from datetime import datetime

from . import db

class Staff(db.Model):
    __tablename__ = 'staff'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    nombre_corto = db.Column(db.String(50))
    puesto = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    pais = db.Column(db.String(50))
    nacimiento = db.Column(db.DateTime)
    creacion = db.Column(db.DateTime, default=datetime.now())

    contrato_staff = db.relationship("ContratoStaff")

    def __init__(self, nombre, nombre_corto, puesto,
                    estado, pais, nacimiento):
        self.nombre = nombre
        self.nombre_corto = nombre_corto
        self.puesto = puesto
        self.estado = estado
        self.pais = pais
        self.nacimiento = nacimiento