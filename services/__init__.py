import os

from flask import Flask
from flask_migrate import Migrate

from flask_cors import CORS

from .models import db
from .models.alineacion import Alineacion
from .models.arbitro import Arbitro
from .models.cambio import Cambio
from .models.club import Club
from .models.contrato_jugador import ContratoJugador
from .models.contrato_staff import ContratoStaff
from .models.estadio import Estadio
from .models.fase import Fase
from .models.gol import Gol
from .models.jugador import Jugador
from .models.liga import Liga
from .models.pago import Pago
from .models.partido import Partido
from .models.sesion import Sesion
from .models.staff import Staff
from .models.tarjeta import Tarjeta
from .models.temporada import Temporada
from .models.usuario import Usuario

from services.api.clubes import club
from services.api.estadios import estadio
from services.api.usuarios import usuario

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.register_blueprint(club, url_prefix="/api/club")
    app.register_blueprint(estadio, url_prefix="/api/estadio")
    app.register_blueprint(usuario, url_prefix="/api/usuario")

    migrate = Migrate(directory="services/migrations")
    migrate.init_app(app, db)

    return app
