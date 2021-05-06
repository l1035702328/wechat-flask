from flask import Blueprint

appPhoto_bp = Blueprint('photo', __name__)


@appPhoto_bp.route("/photo")
def photo():
    return "hello photo"
