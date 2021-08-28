from datetime import datetime

from . import db

class ContratoStaff(db.Model):
    __tablename__ = "contrato_staff"

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,
                            db.ForeignKey("staff.id"))
    club_id = db.Column(db.Integer,
                        db.ForeignKey("club.id"))
    temporada_id = db.Column(db.Integer,
                                db.ForeignKey("temporada.id"))
    creacion = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, staff_id, club_id, temporada_id):
        self.staff_id = staff_id
        self.club_id = club_id
        self.temporada_id = temporada_id