from flask import Blueprint
from controllers.localauth import LocalAuthController

bp = Blueprint("localauth", __name__, url_prefix="/auth")

localAuthController = LocalAuthController()

@bp.route("/login", methods=["GET", "POST"])
def login ():
    return localAuthController.login()