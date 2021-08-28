from flask import Blueprint

from services.utils.responses import response
from services.utils.responses import not_found

from services.models.club import Club
from services.models.club import ClubSchema

club = Blueprint('club', __name__)

@club.route("/all")
def get_all_clubs():

    club_objs = Club.query.all()
    club_schema = ClubSchema(many=True)
    clubes = club_schema.dump(club_objs)

    return response(clubes)

@club.route("/<int:id>")
def get_club(id):

    club_schema = ClubSchema()
    club_obj = Club.query.filter_by(id=id).first()
    club = club_schema.dump(club_obj)

    if len(club) == 0:
        return not_found()

    return response(club)