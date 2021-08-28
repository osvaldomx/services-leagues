from datetime import datetime

from . import db

class Partido(db.Model):
    __tablename__ = 'partido'

    id = db.Column(db.Integer, primary_key=True)
    temporada_id = db.Column(db.Integer, db.ForeignKey("temporada.id"))
    club_local = db.Column(db.Integer, db.ForeignKey("club.id"))
    club_visitante = db.Column(db.Integer, db.ForeignKey("club.id"))
    fecha = db.Column(db.DateTime)
    finalizado = db.Column(db.Integer, default=0)
    t_extra = db.Column(db.Integer, default=0)
    info = db.Column(db.String(250))
    estadio_id = db.Column(db.Integer, db.ForeignKey("estadio.id"))
    jornada = db.Column(db.Integer, default=0)
    goles_local = db.Column(db.Integer, default=0)
    goles_visitante = db.Column(db.Integer, default=0)
    goles_local_mt = db.Column(db.Integer, default=0)
    goles_visitante_mt = db.Column(db.Integer, default=0)
    goles_local_te = db.Column(db.Integer, default=0)
    goles_visitante_te = db.Column(db.Integer, default=0)
    goles_local_penal = db.Column(db.Integer, default=0)
    goles_visitante_penal = db.Column(db.Integer, default=0)
    amarillas_local = db.Column(db.Integer, default=0)
    amarillas_visitante = db.Column(db.Integer, default=0)
    d_amarilla_local = db.Column(db.Integer, default=0)
    d_amarilla_visitante = db.Column(db.Integer, default=0)
    rojas_local = db.Column(db.Integer, default=0)
    rojas_visitante = db.Column(db.Integer, default=0)
    esquina_local = db.Column(db.Integer, default=0)
    esquina_visitante = db.Column(db.Integer, default=0)
    faltas_local = db.Column(db.Integer, default=0)
    faltas_visitante = db.Column(db.Integer, default=0)
    fuera_lugar_local = db.Column(db.Integer, default=0)
    fuera_lugar_visitante = db.Column(db.Integer, default=0)
    posesion_local = db.Column(db.Integer, default=0)
    posesion_visitante = db.Column(db.Integer, default=0)
    disparos_local = db.Column(db.Integer, default=0)
    disparos_visitante = db.Column(db.Integer, default=0)
    disparos_gol_local = db.Column(db.Integer, default=0)
    disparos_gol_visitante = db.Column(db.Integer, default=0)
    arbitro_central = db.Column(db.Integer, db.ForeignKey("arbitro.id"))
    auxiliar1 = db.Column(db.Integer, db.ForeignKey("arbitro.id"))
    auxiliar2 = db.Column(db.Integer, db.ForeignKey("arbitro.id"))
    cuarto_arbitro = db.Column(db.Integer, db.ForeignKey("arbitro.id"))
    creacion = db.Column(db.DateTime, default=datetime.now())

    gol = db.relationship('Gol')
    tarjeta = db.relationship('Tarjeta')
    cambio = db.relationship('Cambio')
    alineacion = db.relationship('Alineacion')

    def __init__(self, temporada_id, club_local, club_visitante, fecha, finalizado,
                    t_extra, info, estadio_id, jornada, goles_local, goles_visitante,
                    goles_local_mt, goles_visitante_mt, goles_local_te,
                    goles_visitante_te, goles_local_penal, goles_visitante_penal,
                    amarillas_local, amarillas_visitante, d_amarilla_local,
                    d_amarilla_visitante, rojas_local, rojas_visitante,
                    esquina_local, esquina_visitante, faltas_local, faltas_visitante,
                    fuera_lugar_local, fuera_lugar_visitante, posesion_local,
                    posesion_visitante, disparos_local, disparos_visitante,
                    disparos_gol_local, disparos_gol_visitante):

        self.temporada_id = temporada_id
        self.club_local = club_local
        self.club_visitante = club_visitante
        self.fecha = fecha
        self.finalizado = finalizado
        self.t_extra = t_extra
        self.info = info
        self.estadio_id = estadio_id
        self.jornada = jornada
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        self.goles_local_mt = goles_local_mt
        self.goles_visitante_mt = goles_visitante_mt
        self.goles_local_te = goles_local_te
        self.goles_visitante_te = goles_visitante_te
        self.goles_local_penal = goles_local_penal
        self.goles_visitante_penal = goles_visitante_penal
        self.amarillas_local = amarillas_local
        self.amarillas_visitante = amarillas_visitante
        self.d_amarilla_local = d_amarilla_local
        self.d_amarilla_visitante = d_amarilla_visitante
        self.rojas_local = rojas_local
        self.rojas_visitante = rojas_visitante
        self.esquina_local = esquina_local
        self.esquina_visitante = esquina_visitante
        self.faltas_local = faltas_local
        self.faltas_visitante = faltas_visitante
        self.fuera_lugar_local = fuera_lugar_local
        self.fuera_lugar_visitante = fuera_lugar_visitante
        self.posesion_local = posesion_local
        self.posesion_visitante = posesion_visitante
        self.disparos_local = disparos_local
        self.disparos_visitante = disparos_visitante
        self.disparos_gol_local = disparos_gol_local
        self.disparos_gol_visitante = disparos_gol_visitante