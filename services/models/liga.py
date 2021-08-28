from datetime import datetime

from . import db

class Liga(db.Model):
    __tablename__ = 'liga'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer,
                            db.ForeignKey("usuario.id"))
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    creacion = db.Column(db.DateTime, default=datetime.now())

    temporada = db.relationship('Temporada')

    def __init__(self, nombre, pais, descripcion):
        self.nombre = nombre
        self.pais = pais
        self.descripcion = descripcion