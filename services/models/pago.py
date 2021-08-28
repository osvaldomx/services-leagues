from datetime import datetime

from marshmallow import Schema
from marshmallow import fields

from . import db

class Pago(db.Model):
    __tablename__ = 'pago'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    cantidad = db.Column(db.Integer, nullable=False)
    creado = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, user_id, cantidad):
        self.user_id = user_id
        self.cantidad = cantidad

class PagoSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    cantidad = fields.Int()
    creado = fields.DateTime()