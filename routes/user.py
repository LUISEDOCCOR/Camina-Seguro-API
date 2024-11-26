from flask import Blueprint
from controllers.user import UserController

bp = Blueprint("auth", __name__, url_prefix="/auth")

userController = UserController()

@bp.post("/signup")
def signup():
    return userController.signup()

@bp.post("/login")
def login():
    return userController.login()
