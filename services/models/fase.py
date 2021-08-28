from datetime import datetime

from . import db

class Fase(db.Model):
    __tablename__ = 'fase'

    id = db.Column(db.Integer, primary_key=True)
    temporada_id = db.Column(db.Integer, db.ForeignKey('temporada.id'))
    nombre = db.Column(db.String(25))
    descripcion = db.Column(db.String(200))
    tipo_fase = db.Column(db.String(25))
    tipo_eliminacion = db.Column(db.String(25))
    creacion = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, temporada_id, nombre, descripcion,
                    tipo_fase, tipo_eliminacion, creacion):
        self.temporada_id = temporada_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo_fase = tipo_fase
        self.tipo_eliminacion = tipo_eliminacion