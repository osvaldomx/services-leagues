from flask import Blueprint

from services.utils.responses import response

from services.models.estadio import Estadio
from services.models.estadio import EstadioSchema

estadio = Blueprint('estadio', __name__)

@estadio.route("/all")
def get_all_estadios():

    estadio_schema = EstadioSchema(many=True)
    estadio_objs = Estadio.query.all()
    estadios = estadio_schema.dump(estadio_objs)

    return response(estadios)