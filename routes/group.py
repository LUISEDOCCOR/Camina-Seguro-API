from flask import Blueprint
from controllers.group import GroupController
from decorators.auth import requires_login
from flask_jwt_extended import jwt_required

bp = Blueprint("group", __name__, url_prefix="/group")

groupController = GroupController()

@bp.get("/")
def getAll ():
    return groupController.getAll()

# WHEN USER IS LOGGED

@bp.post("/")
@jwt_required()
def create ():
    return groupController.create()

@bp.get("/add/<int:id>/<role>")
@jwt_required()
def addPerson (id,role):
    return groupController.addPerson(id, role)

#ADMIN

@bp.get("/changevisibility/<int:id>")
@requires_login
def changeVisibility(id):
    return groupController.changeVisibility(id)

@bp.get("/dashboard")
@requires_login
def dashboard():
    return groupController.dashboard()

@bp.get("/delete/<int:id>")
@requires_login
def delete(id):
    return groupController.delete(id)
